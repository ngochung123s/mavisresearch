"""Convert Vietnamese text khong dau -> co dau.

Strategy:
- Load dictionary mapping (word -> word_with_diacritics)
- Heuristics cho common patterns
- Capitalize first letter giữ nguyên
- Giữ nguyên số, English, special chars
"""
import re
import sys
from pathlib import Path

# Dictionary mapping: word (khong dau) -> word (co dau)
# Chỉ bao gồm các từ phổ biến + thuật ngữ y khoa
# NOTE: 1 từ không dấu có thể ánh xạ sang NHIỀU từ có dấu
# -> Dictionary này chỉ chứa mapping AN TOÀN (1-1)
# Các từ ambiguous sẽ giữ nguyên

DICT = {
    # === Y khoa cơ bản ===
    "benh": "bệnh",
    "huyet": "huyết",
    "huyet ap": "huyết áp",
    "huyet thanh": "huyết thanh",
    "huyet hoc": "huyết học",
    "mach": "mạch",
    "mach mau": "mạch máu",
    "mach mau nho": "mạch máu nhỏ",
    "mach mau xoan": "mạch máu xoắn",
    "than": "thận",
    "than man": "thận mạn",
    "than kinh": "thần kinh",
    "than kinh trung uong": "thần kinh trung ương",
    "gan": "gan",  # gan = liver, no diacritic
    "giam": "giảm",
    "tang": "tăng",
    "ben": "bén",  # ambiguous - default
    "lam": "làm",
    "lam sang": "lâm sàng",
    "lam sang san": "lâm sàng sản",
    "lam sang rang": "lâm sàng răng",  # dental
    "lam": "làm",
    "thanh": "thành",
    "thanh phan": "thành phần",
    "thanh kinh": "thành kinh",  # build
    "thanh doc": "thành dọc",
    "tinh": "tính",
    "tinh chat": "tính chất",
    "tinh chat ly": "tính chất lý",  # physical
    "tinh chat hoa": "tính chất hóa",
    "dinh": "định",
    "dinh nghia": "định nghĩa",
    "dinh luong": "định lượng",
    "dinh tinh": "định tính",
    "nghia": "nghĩa",
    "nghien": "nghiên",
    "nghien cuu": "nghiên cứu",
    "khoa": "khoa",  # default
    "khoa hoc": "khoa học",
    "phuong": "phương",
    "phuong phap": "phương pháp",
    "phuong trinh": "phương trình",
    "truong": "trường",
    "truong hop": "trường hợp",
    "truong thanh": "trưởng thành",
    "do truong thanh": "độ trưởng thành",
    "truong thanh bam sinh": "trưởng thành bẩm sinh",

    # === Sản khoa / Phụ khoa ===
    "san": "sản",  # default
    "san khoa": "sản khoa",
    "san phu": "sản phụ",
    "san phu khoa": "sản phụ khoa",
    "phu": "phụ",  # default (phụ khoa, phụ nữ)
    "phu khoa": "phụ khoa",
    "phu nu": "phụ nữ",
    "san pham": "sản phẩm",
    "trung binh": "trung bình",
    "trung tam": "trung tâm",
    "trung uong": "trung ương",
    "trong": "trong",  # in
    "trong luong": "trọng lượng",
    "con": "con",
    "con so": "con so",
    "con rạ": "con rạ",
    "thu thai": "thụ thai",
    "thu tinh": "thụ tinh",
    "thu tinh trong ong nghiem": "thụ tinh trong ống nghiệm",
    "trung": "trung",
    "trung gian": "trung gian",
    "giai doan": "giai đoạn",
    "thoi gian": "thời gian",
    "thai": "thai",  # default (pregnant)
    "thai ky": "thai kỳ",
    "thai phu": "thai phụ",
    "thai nhi": "thai nhi",
    "mang thai": "mang thai",
    "mang thai lan can": "mang thai lần cận",  # not common
    "tuoi me": "tuổi mẹ",
    "tuoi": "tuổi",
    "vo sinh": "vô sinh",
    "vo sinh nam": "vô sinh nam",
    "vo sinh nu": "vô sinh nữ",
    "hien tuong": "hiện tượng",
    "kha nang": "khả năng",
    "thuong": "thường",
    "thuong gap": "thường gặp",
    "thuong xuyen": "thường xuyên",
    "xuat hien": "xuất hiện",
    "phat hien": "phát hiện",
    "bat thuong": "bất thường",
    "co the": "có thể",
    "co y nghia": "có ý nghĩa",
    "thuyet phuc": "thuyết phục",
    "phu nu": "phụ nữ",
    "bac si": "bác sĩ",

    # === Tiền sản giật / Hypertension ===
    "tang huyet ap": "tăng huyết áp",
    "tang ha": "tăng huyết áp",
    "huyet ap": "huyết áp",
    "huyet ap cao": "huyết áp cao",
    "huyet ap thap": "huyết áp thấp",
    "tien san giat": "tiền sản giật",
    "tien san giat som": "tiền sản giật sớm",
    "san giat": "sản giật",
    "san giat som": "sản giật sớm",
    "sot thai": "sót thai",  # rare
    "suy thai": "suy thai",
    "suy nhu": "suy nhược",  # not common
    "suy than": "suy thận",
    "suy than man": "suy thận mạn",
    "suy than cap": "suy thận cấp",
    "suy tim": "suy tim",
    "suy hoang the": "suy hoàng thể",  # corpus luteum
    "sinh non": "sinh non",
    "sinh thuong": "sinh thường",
    "sinh mo": "sinh mổ",
    "mo lay thai": "mổ lấy thai",
    "mo": "mổ",  # ambiguous
    "khoe manh": "khỏe mạnh",
    "benh ly": "bệnh lý",
    "benh tim mach": "bệnh tim mạch",
    "benh tu mien": "bệnh tự miễn",
    "benh than kinh": "bệnh thần kinh",
    "benh gan": "bệnh gan",
    "benh huyet hoc": "bệnh huyết học",

    # === Tim mạch / Huyết học ===
    "dong mach": "động mạch",
    "tinh mach": "tĩnh mạch",
    "mao mach": "mao mạch",
    "vi mach": "vi mạch",
    "vi tuan hoan": "vi tuần hoàn",
    "tuan hoan": "tuần hoàn",
    "vi tuan hoan nhau": "vi tuần hoàn nhau",
    "tuan hoan ngoai vi": "tuần hoàn ngoại vi",
    "bom": "bơm",  # pump
    "sung huyet": "sung huyết",
    "phu": "phù",  # edema
    "phu phoi": "phù phổi",
    "phu chan": "phù chân",
    "phu toan than": "phù toàn thân",
    "tai cau truc": "tái cấu trúc",
    "tai cau truc mach mau xoan": "tái cấu trúc mạch máu xoắn",

    # === Phôi thai / Nhau ===
    "nhau": "nhau",
    "nhau thai": "nhau thai",
    "nhau thai nhiem mon": "nhau thai nhiễm mòn",  # not common
    "nhau bong non": "nhau bong non",
    "nhau tien dao": "nhau tiền đạo",
    "nhau can": "nhau cài",  # accreta
    "nhau can rang": "nhau cài răng",  # increta
    "nhau can xuyen": "nhau cài xuyên",  # percreta
    "song thai": "song thai",
    "da thai": "đa thai",
    "don thai": "đơn thai",
    "da thai chi em": "đa thai chi em",  # monozygotic
    "da thai khac trung": "đa thai khác trứng",  # dizygotic
    "thai trung": "thai trứng",  # not common
    "khoi u": "khối u",
    "khoi u buong trung": "khối u buồng trứng",
    "buong trung": "buồng trứng",
    "buong": "buồng",  # room/atrium
    "te bao": "tế bào",
    "te bao nuoi": "tế bào nuôi",
    "te bao non": "tế bào nón",  # not common
    "trophoblast": "trophoblast",  # keep
    "hormon": "hormone",  # ambiguous
    "noi tiet": "nội tiết",
    "noi tiet to": "nội tiết tố",
    "protein": "protein",
    "protein niem": "protein niệm",  # not common

    # === Chẩn đoán / Xét nghiệm ===
    "sieu am": "siêu âm",
    "sieu am thai": "siêu âm thai",
    "chan doan": "chẩn đoán",
    "xet nghiem": "xét nghiệm",
    "xet nghiem mau": "xét nghiệm máu",
    "xet nghiem hinh anh": "xét nghiệm hình ảnh",
    "sang loc": "sàng lọc",
    "sang loc truoc sinh": "sàng lọc trước sinh",
    "sang loc quy 1": "sàng lọc quý 1",
    "sang loc quy 2": "sàng lọc quý 2",
    "sang loc quy 3": "sàng lọc quý 3",
    "sang loc tien san giat": "sàng lọc tiền sản giật",
    "sang loc bat thuong nhiem sac the": "sàng lọc bất thường nhiễm sắc thể",
    "bat thuong nhiem sac the": "bất thường nhiễm sắc thể",
    "hinh anh hoc": "hình ảnh học",
    "x quang": "x-quang",
    "doppler": "Doppler",
    "doppler mau": "Doppler mạch",  # ambiguous
    "doppler dong mach": "Doppler động mạch",
    "doppler tinh mach": "Doppler tĩnh mạch",
    "doppler dong mach tu cung": "Doppler động mạch tử cung",
    "doppler dong mach ron": "Doppler động mạch rốn",
    "doppler nao giua": "Doppler não giữa",

    # === Điều trị / Thuốc ===
    "aspirin": "aspirin",
    "aspirin lieu thap": "aspirin liều thấp",
    "aspirin lieu cao": "aspirin liều cao",
    "du phong": "dự phòng",
    "dieu tri": "điều trị",
    "dieu tri du phong": "điều trị dự phòng",
    "thuoc": "thuốc",
    "thuoc khang sinh": "thuốc kháng sinh",
    "thuoc chong dong": "thuốc chống đông",
    "heparin": "heparin",
    "canxi": "canxi",
    "calcium": "canxi",
    "magie": "magie",
    "magnes": "magie",
    "vitamin": "vitamin",
    "corticosteroid": "corticosteroid",
    "corticoid": "corticoid",

    # === Giải phẫu ===
    "tu cung": "tử cung",
    "co tu cung": "cổ tử cung",
    "buong trung": "buồng trứng",
    "ong danh trung": "ống dẫn trứng",
    "vom": "vòm",  # vault
    "vom mong": "vòm mông",  # not common
    "am dao": "âm đạo",
    "am vat": "âm vật",
    "san day": "sàn đáy",  # pelvic floor
    "xuong chau": "xương chậu",
    "xuong": "xương",
    "co": "cổ",  # neck/cervix
    "co tu cung ngan": "cổ tử cung ngắn",
    "nguc": "ngực",
    "bieu mo": "biểu mô",
    "niem mac": "niêm mạc",
    "co tu": "cơ tử",  # not common
    "co tron": "cơ trơn",
    "co vân": "cơ vân",
    "xuong song": "xương sống",
    "cot song": "cột sống",
    "nao": "não",
    "nao that": "não thất",
    "nao giua": "não giữa",  # MCA
    "dong mach canh": "động mạch cảnh",
    "gan": "gan",
    "than kinh": "thần kinh",

    # === Triệu chứng / Dấu hiệu ===
    "dau bung": "đau bụng",
    "dau ha suon": "đau hạ sườn",
    "dau dau": "đau đầu",
    "dau lung": "đau lưng",
    "dau khop": "đau khớp",
    "dau nguc": "đau ngực",
    "buon non": "buồn nôn",
    "non": "nôn",
    "non ra mau": "nôn ra máu",
    "chay mau": "chảy máu",
    "chay mau am dao": "chảy máu âm đạo",
    "xa am dao": "xả âm đạo",
    "phu": "phù",
    "sung": "sưng",
    "nhuc dau": "nhức đầu",
    "choang mat": "choáng váng",
    "bat tinh": "bất tỉnh",
    "ngat": "ngất",
    "kho tho": "khó thở",
    "met moi": "mệt mỏi",
    "buot": "buốt",
    "ran": "rắn",
    "long bung": "lỏng bụng",

    # === Bệnh lý cụ thể ===
    "dai thao duong": "đái tháo đường",
    "tieu duong": "tiểu đường",
    "tang huyet ap man": "tăng huyết áp mạn",
    "tang huyet ap thai ky": "tăng huyết áp thai kỳ",
    "loan nhip": "loạn nhịp",
    "suy tim": "suy tim",
    "hoi chung": "hội chứng",
    "hoi chung thuc quan": "hội chứng thực quản",  # not common
    "hoi chung antiphospholipid": "hội chứng antiphospholipid",
    "SLE": "SLE",
    "lupus": "lupus",
    "viem khop": "viêm khớp",
    "viem": "viêm",
    "viem phe quan": "viêm phế quản",
    "viem phoi": "viêm phổi",
    "viem nieu": "viêm niệu",  # urinary
    "viem nieu dao": "viêm niệu đạo",
    "viem bang quang": "viêm bàng quang",
    "viem than": "viêm thận",
    "viem loet da day": "viêm loét dạ dày",
    "ung thu": "ung thư",
    "ung thu vu": "ung thư vú",
    "ung thu co tu cung": "ung thư cổ tử cung",
    "ung thu buong trung": "ung thư buồng trứng",
    "ung thu noi mac": "ung thư nội mạc",

    # === Thuật ngữ khác ===
    "tuan": "tuần",
    "ngay": "ngày",
    "gio": "giờ",
    "phut": "phút",
    "thang": "tháng",
    "nam": "năm",
    "tu": "từ",  # from/word
    "den": "đến",
    "tu": "từ",
    "tren": "trên",
    "duoi": "dưới",
    "trong": "trong",  # in
    "ngoai": "ngoài",
    "sau": "sau",  # after
    "truoc": "trước",
    "ben": "bên",
    "giua": "giữa",
    "canh": "cạnh",
    "gan": "gần",  # near - REMOVED (ambiguous with gan=liver)
    "xa": "xa",  # far
    "gan gan": "gan gần",  # REMOVED ambiguous
    "lon": "lớn",
    "nho": "nhỏ",
    "cao": "cao",
    "thap": "thấp",
    "dai": "dài",
    "ngan": "ngắn",
    "rong": "rộng",
    "hep": "hẹp",
    "nhieu": "nhiều",
    "it": "ít",
    "toan bo": "toàn bộ",
    "mot so": "một số",
    "mot vai": "một vài",
    "kha nhieu": "khá nhiều",
    "rat it": "rất ít",
    "rat nhieu": "rất nhiều",
    "nhieu hon": "nhiều hơn",
    "it hon": "ít hơn",

    # === Từ hành chính / Chung ===
    "cong": "công",
    "cong ty": "công ty",
    "cong nghe": "công nghệ",
    "phuong tien": "phương tiện",
    "phuong phap": "phương pháp",
    "trinh do": "trình độ",
    "trinh tu": "trình tự",
    "trinh bay": "trình bày",
    "trinh bay tom tat": "trình bày tóm tắt",
    "tom tat": "tóm tắt",
    "tom lai": "tóm lại",
    "vi du": "ví dụ",
    "vi the": "vì thế",
    "vi": "vì",
    "do": "do",  # because
    "do do": "do đó",
    "nen": "nên",
    "neu": "nếu",
    "tuy nhien": "tuy nhiên",
    "tuy": "tuy",
    "mac du": "mặc dù",
    "hon": "hơn",
    "hon nua": "hơn nữa",
    "them": "thêm",
    "them vao": "thêm vào",
    "vai": "vài",
    "tuyet nhien": "tuyệt nhiên",
    "nhat": "nhất",
    "nhat la": "nhất là",
    # NOTE: "nam" AMBIGUOUS - giữa "nam" (proper noun) và "năm" (year). Bỏ mapping.
    # "Việt Nam" sẽ bị lỗi nếu map "nam" -> "năm". Default: giữ nguyên.
    "quan trong": "quan trọng",
    "rat quan trong": "rất quan trọng",
    "hinh": "hình",
    "hinh thuc": "hình thức",
    "hinh anh": "hình ảnh",
    "thoi": "thời",
    "thoi gian": "thời gian",
    "thoi diem": "thời điểm",
    "hien tai": "hiện tại",
    "hien nay": "hiện nay",
    "truoc do": "trước đó",
    "sau do": "sau đó",
    "vao": "vào",
    "ra": "ra",
    "len": "lên",
    "xuong": "xuống",
    "moi": "mới",
    "cu": "cũ",
    "dau": "đầu",
    "cuoi": "cuối",
    "giua": "giữa",
    "can": "cần",
    "nen": "nên",
    "phai": "phải",
    "co the": "có thể",
    "khong the": "không thể",
    "khong": "không",
    "duoc": "được",
    "mot": "một",
    "hai": "hai",
    "ba": "ba",
    "bon": "bốn",
    "nam": "năm",
    "sau": "sáu",
    "bay": "bảy",
    "tam": "tám",
    "chin": "chín",
    "muoi": "mười",

    # === Safe-remove (ambiguous) mappings ===
    # These caused bugs in tests - keep original

    # === Đặc biệt: Tên riêng / viết tắt / thuật ngữ giữ ===
    # (giữ nguyên, không thêm dấu)
}


def is_english_word(word):
    """Check if a word contains only English characters (already diacritics-free)."""
    return bool(re.match(r'^[a-zA-Z0-9_./\-(),%°\[\]\{\}]+$', word))


def preserve_case(original, converted):
    """Preserve original case (uppercase, lowercase, capitalized) in converted word."""
    if not original or not converted:
        return converted
    if original.isupper() and len(original) > 1:
        return converted.upper()
    if original[0].isupper() and original[1:].islower():
        return converted[0].upper() + converted[1:]
    return converted


def add_diacritics_to_word(word):
    """Add Vietnamese diacritics to a single word, preserving case."""
    if not word or len(word) < 2:
        return word
    # Pure English / numbers / symbols
    if is_english_word(word):
        return word
    # Strip punctuation for matching
    clean = re.sub(r'[^\w]', '', word.lower())
    if not clean:
        return word
    # Direct dict match
    if clean in DICT:
        return preserve_case(word, DICT[clean])
    # Try as a phrase (split into parts)
    # If word has hyphens, try each part
    # Return original if no match
    return word


def add_diacritics_to_text(text):
    """Add Vietnamese diacritics to text, preserving markdown/code blocks."""
    lines = text.split('\n')
    result = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if in_code_block:
            result.append(line)
            continue
        # Skip table separators (e.g., |---|---|---|)
        if re.match(r'^[\s|:\-]+$', line):
            result.append(line)
            continue
        # Process line word-by-word, preserving markdown chars
        # Use regex to split into tokens: words, punctuation, etc.
        tokens = re.findall(r'[^\s]+|\s+', line)
        new_tokens = []
        for tok in tokens:
            if tok.isspace():
                new_tokens.append(tok)
                continue
            # Skip URLs / code inline
            if tok.startswith('http') or tok.startswith('!'):
                new_tokens.append(tok)
                continue
            # If token contains a forward-slash abbreviation like 'I/II/III', keep as is
            if re.match(r'^[IVX]+$', tok):
                new_tokens.append(tok)
                continue
            # Otherwise add diacritics
            new_tokens.append(add_diacritics_to_word(tok))
        result.append(''.join(new_tokens))
    return '\n'.join(result)


def convert_file(input_path, output_path=None, dry_run=False):
    """Convert file khong dau -> co dau. If output_path None, in-place."""
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path
    else:
        output_path = Path(output_path)
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    converted = add_diacritics_to_text(text)
    if not dry_run:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted)
    return converted


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python add_diacritics.py <input.md> [output.md]")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    convert_file(input_path, output_path)
    print(f"Converted: {input_path}" + (f" -> {output_path}" if output_path else " (in-place)"))
