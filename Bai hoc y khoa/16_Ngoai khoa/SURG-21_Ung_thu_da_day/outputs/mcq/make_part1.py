import json

part1 = [
    {
        "id": "SURG21-A01",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Dịch tễ học ung thư dạ dày thế giới",
        "bloom": "nhớ",
        "difficulty": 1,
        "source": "SURG-21 §1.1",
        "text": "Theo số liệu dịch tễ học ung thư dạ dày được ghi nhận tại Nhật Bản trong giáo trình, đặc điểm tỷ lệ mắc thô và độ tuổi trung bình khi chẩn đoán là bao nhiêu?",
        "options": [
            "Tỷ lệ mắc 69/100.000 dân với độ tuổi trung bình khi chẩn đoán là 55 tuổi.",
            "Tỷ lệ mắc 28/100.000 dân với độ tuổi trung bình khi chẩn đoán là 63 tuổi.",
            "Tỷ lệ mắc 25,7/100.000 dân với độ tuổi trung bình khi chẩn đoán là 50–60 tuổi.",
            "Tỷ lệ mắc 5/100.000 dân với độ tuổi trung bình khi chẩn đoán là 63 tuổi."
        ],
        "correct": 0,
        "explanation": "Theo mục 1.1 giáo trình: Tại Nhật Bản, tỷ lệ ung thư dạ dày là 69/100.000 dân, tuổi trung bình là 55. Tại Mỹ ở nam giảm từ 28/100.000 xuống 5/100.000, tuổi trung bình là 63. Tại Hà Nội tỷ lệ nam là 25,7/100.000.",
        "option_explanations": [
            "Đúng — Khớp tuyệt đối số liệu dịch tễ học Nhật Bản trong barem (§1.1): tỷ lệ mắc 69/100.000 dân, tuổi trung bình 55.",
            "Sai — 28/100.000 là tỷ lệ mắc trước đây ở nam giới tại Mỹ, tuổi trung bình 63 tuổi là số liệu tại Mỹ (§1.1).",
            "Sai — 25,7/100.000 dân là tần suất mắc ở nam giới tại Hà Nội (giai đoạn 1993–1995), tuổi 50–60 là độ tuổi thường gặp tại Việt Nam (§1.1).",
            "Sai — 5/100.000 dân là tỷ lệ mắc ở nam giới tại Mỹ những năm gần đây (§1.1)."
        ]
    },
    {
        "id": "SURG21-A02",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Dịch tễ học ung thư dạ dày tại Việt Nam",
        "bloom": "hiểu",
        "difficulty": 1,
        "source": "SURG-21 §1.1",
        "text": "Tại Việt Nam, tần suất mắc ung thư dạ dày ghi nhận theo các nghiên cứu dịch tễ học (Hà Nội 1993–1995 và TP. Hồ Chí Minh 1997) và thứ hạng theo giới tính có đặc điểm nào sau đây?",
        "options": [
            "Đứng hàng thứ 2 ở nam (sau ung thư phế quản) và thứ 2 ở nữ (sau ung thư vú), tỷ lệ nam/nữ là 2/1.",
            "Đứng hàng thứ 1 ở nam (trên ung thư phế quản) và thứ 3 ở nữ (sau ung thư cổ tử cung và vú), tỷ lệ nam/nữ là 1,7/1.",
            "Đứng hàng thứ 3 ở nam (sau ung thư gan và phế quản) và thứ 1 ở nữ (trên ung thư vú), tỷ lệ nam/nữ là 3/1.",
            "Đứng hàng thứ 2 ở nam (sau ung thư đại trực tràng) và thứ 4 ở nữ (sau ung thư vú), tỷ lệ nam/nữ là 1/1."
        ],
        "correct": 0,
        "explanation": "Theo mục 1.1 barem: Tại Việt Nam, ung thư dạ dày đứng thứ 2 ở nam giới (sau ung thư phế quản) và thứ 2 ở nữ giới (sau ung thư vú). Tỷ lệ nam/nữ là 2/1. Tỷ lệ nam/nữ 1,7/1 là số liệu tại Mỹ.",
        "option_explanations": [
            "Đúng — Phản ánh chính xác dịch tễ học Việt Nam (§1.1): đứng thứ 2 ở nam (sau phế quản) và thứ 2 ở nữ (sau vú), tỷ lệ nam/nữ là 2/1.",
            "Sai — Tỷ lệ nam/nữ 1,7/1 là số liệu tại Mỹ (§1.1), ung thư dạ dày ở VN đứng thứ 2 sau phế quản chứ không đứng hàng thứ 1.",
            "Sai — Ung thư dạ dày ở VN không đứng hàng thứ 3 ở nam và không đứng thứ 1 ở nữ; tỷ lệ nam/nữ trong barem là 2/1 chứ không phải 3/1.",
            "Sai — Tại Việt Nam ung thư dạ dày đứng sau ung thư phế quản ở nam và sau ung thư vú ở nữ, không phải xếp sau đại trực tràng."
        ]
    },
    {
        "id": "SURG21-A03",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Dịch tễ học chủng tộc và kinh tế xã hội",
        "bloom": "hiểu",
        "difficulty": 2,
        "source": "SURG-21 §1.1",
        "text": "Khi phân tích mối liên quan giữa chủng tộc, điều kiện kinh tế xã hội và nguy cơ mắc ung thư dạ dày tại Mỹ theo giáo trình, nhận định nào sau đây là chính xác?",
        "options": [
            "Người Mỹ gốc da đen, da đỏ và gốc Tây Ban Nha có tỷ lệ ung thư dạ dày gấp 2 lần so với người Mỹ da trắng; nguy cơ cao ở tầng lớp kinh tế xã hội thấp.",
            "Người Mỹ da trắng có tỷ lệ ung thư dạ dày cao gấp 2 lần so với người Mỹ gốc da đen; nguy cơ mắc tập trung ở tầng lớp kinh tế xã hội cao.",
            "Người Mỹ gốc Á có tỷ lệ ung thư dạ dày thấp hơn 2 lần so với người Mỹ da trắng; điều kiện kinh tế xã hội không ảnh hưởng đến tỷ lệ mắc.",
            "Người Mỹ gốc Tây Ban Nha có tỷ lệ ung thư dạ dày tương đương người da trắng; tỷ lệ tử vong chỉ giảm ở nhóm kinh tế xã hội cao."
        ],
        "correct": 0,
        "explanation": "Barem §1.1 ghi rõ: 'tần suất mắc bệnh có liên quan đến chủng tộc (người Mỹ gốc da đen, da đỏ và gốc Tây Ban Nha tỷ lệ ung thư gấp 2 lần so với người Mỹ da trắng). Về dịch tễ học, nguy cơ ung thư dạ dày cao ở tầng lớp có đời sống kinh tế xã hội thấp.'",
        "option_explanations": [
            "Đúng — Đúng từng câu chữ theo barem §1.1 về yếu tố chủng tộc tại Mỹ và tầng lớp kinh tế xã hội thấp.",
            "Sai — Barem nêu rõ người da đen, da đỏ, gốc Tây Ban Nha gấp 2 lần người da trắng và nguy cơ cao ở tầng lớp kinh tế xã hội thấp, không phải người da trắng cao hơn.",
            "Sai — Barem không so sánh người Mỹ gốc Á mà nêu rõ các chủng tộc da đen, da đỏ, Tây Ban Nha cao gấp 2 lần da trắng; yếu tố kinh tế xã hội thấp làm tăng nguy cơ rõ rệt.",
            "Sai — Người gốc Tây Ban Nha có tỷ lệ mắc gấp 2 lần người da trắng, không phải tương đương."
        ]
    },
    {
        "id": "SURG21-A04",
        "type": "vignette",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Yếu tố môi trường và chế độ ăn",
        "bloom": "vận dụng",
        "difficulty": 2,
        "source": "SURG-21 §1.2",
        "text": "Một nghiên cứu theo dõi đoàn hệ những người Nhật Bản di cư sang sinh sống lâu năm tại Hoa Kỳ ghi nhận tỷ lệ mắc ung thư dạ dày ở thế hệ sau giảm rõ rệt tiệm cận mức của cư dân bản địa Hoa Kỳ. Bằng chứng dịch tễ học này minh chứng rõ nhất cho vai trò của yếu tố nào sau đây trong sinh bệnh học ung thư dạ dày?",
        "options": [
            "Yếu tố môi trường sống và thói quen ẩm thực đóng vai trò chủ đạo làm thay đổi nguy cơ mắc bệnh.",
            "Đột biến mất đoạn gen ức chế khối u p53 mang tính di truyền cố định qua các thế hệ gia tộc.",
            "Tỷ lệ kháng thể kháng tế bào thành dạ dày trong bệnh thiếu máu Biermer tự phục hồi theo địa lý.",
            "Tỷ lệ người mang kháng nguyên hồng cầu nhóm máu A suy giảm dần theo thế hệ di cư."
        ],
        "correct": 0,
        "explanation": "Theo mục 1.2: Yếu tố môi trường giữ vai trò quan trọng (người Nhật Bản di cư sang Mỹ có tỷ lệ mắc bệnh giảm thấp theo môi trường mới).",
        "option_explanations": [
            "Đúng — Barem §1.2 dẫn chứng trực tiếp: người Nhật Bản di cư sang Mỹ có tỷ lệ mắc bệnh giảm thấp theo môi trường mới, chứng minh vai trò chủ đạo của môi trường và chế độ ăn.",
            "Sai — Đột biến gen p53 là yếu tố gen (§1.2), biến đổi cố định theo hệ gen di truyền chứ không giải thích hiện tượng giảm tần suất nhanh chóng khi thay đổi môi trường sống.",
            "Sai — Bệnh Biermer là bệnh lý tiền ung thư tự miễn (§1.2), không phải cơ chế giải thích dịch tễ di cư Nhật - Mỹ.",
            "Sai — Nhóm máu A là yếu tố di truyền cố định (§1.2), không thay đổi tỷ lệ mắc bệnh theo môi trường mới."
        ]
    },
    {
        "id": "SURG21-A05",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Hóa chất sinh ung và chất bảo vệ",
        "bloom": "hiểu",
        "difficulty": 2,
        "source": "SURG-21 §1.2",
        "text": "Trong cơ chế phát sinh ung thư dạ dày do chế độ ăn uống được nêu trong giáo trình, nhóm chất nào sau đây có nguy cơ gây ung thư cao và vi chất nào có vai trò trung hòa các chất sinh ung thư này?",
        "options": [
            "Thực phẩm chứa nhiều Nitrosamin, Nitrates, Nitrites; được trung hòa bởi thức ăn chứa nhiều vitamin C.",
            "Thực phẩm chứa nhiều tồn dư hóa chất hữu cơ bảo quản; được trung hòa bởi thức ăn giàu vitamin A và kẽm.",
            "Thực phẩm giàu acid béo no chuỗi dài; được trung hòa bởi chế độ bổ sung dịch dạ dày nhân tạo chứa toan.",
            "Thực phẩm lên men chua tự nhiên; được trung hòa bởi các hợp chất kháng thể đơn dòng kháng HER2-neu."
        ],
        "correct": 0,
        "explanation": "Barem §1.2: Thức ăn hun khói, thức ăn khô, thực phẩm bảo quản nhiều muối, thức ăn chứa nhiều Nitrosamin, Nitrates, Nitrites liên quan chặt chẽ đến UTDD. Thức ăn chứa nhiều vitamin C (cam, chanh) có thể trung hòa các chất gây ung thư.",
        "option_explanations": [
            "Đúng — Trích đúng barem §1.2: Nitrosamin, Nitrates, Nitrites từ thực phẩm muối/hun khói làm tăng nguy cơ ung thư; thức ăn chứa nhiều vitamin C (cam, chanh) có thể trung hòa các chất gây ung thư.",
            "Sai — Barem §1.2 đề cập vitamin C (cam, chanh), không đề cập vai trò trung hòa của vitamin A hay kẽm.",
            "Sai — Barem §1.2 không nêu acid béo no chuỗi dài và dịch dạ dày toan nhân tạo trong cơ chế sinh ung của chế độ ăn.",
            "Sai — Kháng thể đơn dòng kháng HER2-neu là thuốc điều trị đích Trastuzumab ở giai đoạn điều trị (§6.3), không phải vi chất dinh dưỡng."
        ]
    },
    {
        "id": "SURG21-A06",
        "type": "vignette",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Nhiễm Helicobacter pylori và Béo phì",
        "bloom": "nhớ",
        "difficulty": 1,
        "source": "SURG-21 §1.2",
        "text": "Một nam bệnh nhân 52 tuổi đến khám kiểm tra sức khỏe. Bệnh nhân có chỉ số BMI 32 kg/m² và test hơi thở dương tính với vi khuẩn Helicobacter pylori (HP). Theo số liệu dịch tễ học nêu trong giáo trình, tỷ lệ dân số nhiễm HP và mức độ gia tăng nguy cơ ung thư dạ dày do béo phì là bao nhiêu?",
        "options": [
            "Khoảng 70% dân số nhiễm vi khuẩn HP; béo phì làm tăng nguy cơ mắc ung thư dạ dày cao gấp 2 lần.",
            "Khoảng 50% dân số nhiễm vi khuẩn HP; béo phì làm tăng nguy cơ mắc ung thư dạ dày cao gấp 4 lần.",
            "Khoảng 80% dân số nhiễm vi khuẩn HP; béo phì làm tăng nguy cơ mắc ung thư dạ dày cao gấp 1,5 lần.",
            "Khoảng 30% dân số nhiễm vi khuẩn HP; béo phì làm tăng nguy cơ mắc ung thư dạ dày cao gấp 3 lần."
        ],
        "correct": 0,
        "explanation": "Theo mục 1.2: Khoảng 70% dân số nhiễm vi khuẩn HP – yếu tố làm tăng nguy cơ mắc UTDD và là yếu tố hàng đầu tại Việt Nam. Béo phì làm tăng nguy cơ mắc ung thư dạ dày cao gấp 2 lần.",
        "option_explanations": [
            "Đúng — Khớp chính xác số liệu trong barem §1.2: HP nhiễm ở khoảng 70% dân số (yếu tố hàng đầu tại VN), béo phì tăng nguy cơ gấp 2 lần.",
            "Sai — Tỷ lệ nhiễm HP trong barem là 70%, nguy cơ do béo phì là gấp 2 lần chứ không phải gấp 4 lần.",
            "Sai — Con số 80% trong bài là tỷ lệ ung thư dạ dày giai đoạn sớm không có triệu chứng (§3.1), không phải tỷ lệ nhiễm HP.",
            "Sai — Tỷ lệ nhiễm HP 30% và nguy cơ gấp 3 lần không đúng với số liệu được công bố trong barem §1.2."
        ]
    },
    {
        "id": "SURG21-A07",
        "type": "vignette",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Bệnh lý tiền ung thư dạ dày",
        "bloom": "vận dụng",
        "difficulty": 2,
        "source": "SURG-21 §1.2 & Câu hỏi lượng giá 2",
        "text": "Một bác sĩ ngoại khoa đang lập kế hoạch tầm soát ung thư dạ dày cho các bệnh nhân có cơ địa tiền ung thư mạn tính. Dựa theo các tình trạng bệnh lý tiền ung thư (yếu tố thuận lợi) được xác định trong giáo trình, bệnh nhân nào sau đây KHÔNG thuộc nhóm cơ địa tiền ung thư kinh điển của ung thư dạ dày?",
        "options": [
            "Bệnh nhân 45 tuổi có tiền sử phẫu thuật cắt dây thần kinh X chọn lọc do loét hành tá tràng cách đây 5 năm.",
            "Bệnh nhân 60 tuổi có tiền sử phẫu thuật cắt đoạn dạ dày nối Billroth II do loét lành tính cách đây 12 năm.",
            "Bệnh nhân 55 tuổi được chẩn đoán viêm teo dạ dày mạn tính kèm tình trạng vô toan dịch vị.",
            "Bệnh nhân 50 tuổi được điều trị thiếu máu ác tính Biermer do kháng thể kháng yếu tố nội tại."
        ],
        "correct": 0,
        "explanation": "Theo mục 1.2 và Câu hỏi lượng giá 2 trong barem: Các cơ địa dễ mắc UTDD gồm: cắt đoạn dạ dày sau 10-15 năm, viêm teo dạ dày mạn tính, vô toan, thiếu máu ác tính Biermer, u tuyến (polyp) dạ dày. Cắt dây thần kinh X KHÔNG phải là cơ địa nguy cơ cao kinh điển của ung thư dạ dày (Đáp án B trong Câu hỏi lượng giá 2).",
        "option_explanations": [
            "Đúng — Cắt dây thần kinh X không nằm trong nhóm cơ địa tiền ung thư (Câu hỏi lượng giá 2 trong barem chỉ rõ: cơ địa kinh điển ngoại trừ những người đã cắt dây thần kinh X).",
            "Sai — Cắt đoạn dạ dày sau 10–15 năm là bệnh lý tiền ung thư điển hình được ghi rõ tại §1.2 và Câu hỏi lượng giá 2.",
            "Sai — Viêm teo dạ dày mạn tính kèm vô toan là yếu tố thuận lợi tiền ung thư được nêu rõ tại §1.2 và Câu hỏi lượng giá 2.",
            "Sai — Thiếu máu ác tính Biermer là bệnh lý tiền ung thư kinh điển được nêu rõ tại §1.2 và Câu hỏi lượng giá 2."
        ]
    },
    {
        "id": "SURG21-A08",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Đường lây truyền vi khuẩn Helicobacter pylori",
        "bloom": "hiểu",
        "difficulty": 2,
        "source": "SURG-21 §1.2 & Câu hỏi lượng giá 1",
        "text": "Khi phân tích các yếu tố nguy cơ dẫn đến ung thư dạ dày theo tài liệu giảng dạy, nhận định nào sau đây là KHÔNG chính xác về yếu tố nguy cơ và đường lây truyền của Helicobacter pylori?",
        "options": [
            "Nhiễm Helicobacter pylori qua nguồn nước uống trực tiếp chứa nồng độ vi khuẩn cao.",
            "Thường xuyên sử dụng thịt, cá ướp nhiều muối hoặc thực phẩm hun khói, sấy khô.",
            "Sử dụng nguồn nước sinh hoạt hoặc thực phẩm có chứa hàm lượng nitrate cao.",
            "Tiền sử hút nhiều thuốc lá và tiêu thụ lượng lớn rượu bia kéo dài."
        ],
        "correct": 0,
        "explanation": "Theo Câu hỏi lượng giá 1 và mục 1.2: Các yếu tố nguy cơ gồm thịt cá ướp muối/hun khói, hút thuốc lá, uống nhiều rượu, nước chứa nhiều nitrate. Nhận định sai là 'Uống nước có nhiều Helicobacter pylori' vì HP lây truyền qua đường miệng-miệng hoặc phân-miệng, không gọi là uống nước có nhiều HP.",
        "option_explanations": [
            "Đúng — Câu hỏi lượng giá 1 trong barem khẳng định phương án ngoại trừ là 'Uống nước có nhiều Helicobacter Pylori' (HP lây truyền qua đường miệng-miệng hoặc phân-miệng, không gọi là uống nước có nhiều HP).",
            "Sai — Thịt cá ướp muối/hun khói là yếu tố nguy cơ điển hình được ghi nhận tại Câu hỏi lượng giá 1 và mục 1.2.",
            "Sai — Nước chứa nhiều nitrate là tiền chất tạo nitrosamin sinh ung thư, là yếu tố nguy cơ thật nêu tại Câu hỏi lượng giá 1 và mục 1.2.",
            "Sai — Thuốc lá và rượu là các yếu tố nguy cơ được đề cập tại Câu hỏi lượng giá 1."
        ]
    },
    {
        "id": "SURG21-A09",
        "type": "concept",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Yếu tố di truyền và đột biến gen",
        "bloom": "nhớ",
        "difficulty": 1,
        "source": "SURG-21 §1.2",
        "text": "Về yếu tố di truyền và gen học trong ung thư dạ dày, giáo trình ghi nhận nhóm máu hệ ABO nào có tỷ lệ mắc cao hơn và đột biến gen nào có liên quan trực tiếp?",
        "options": [
            "Người có nhóm máu A có tỷ lệ mắc cao hơn; liên quan đến đột biến gen ức chế khối u p53.",
            "Người có nhóm máu O có tỷ lệ mắc cao hơn; liên quan đến đột biến gen thụ thể HER2-neu.",
            "Người có nhóm máu B có tỷ lệ mắc cao hơn; liên quan đến đột biến gen sửa chữa sai sót ghép cặp mismatch.",
            "Người có nhóm máu AB có tỷ lệ mắc cao hơn; liên quan đến chuyển đoạn nhiễm sắc thể Philadelphia."
        ],
        "correct": 0,
        "explanation": "Barem §1.2 nêu rõ: Nhóm máu A có tỷ lệ UTDD cao hơn. Gia đình có tính chất di truyền (dòng họ Gauser 174 người có 41 người ung thư dạ dày; gia tộc Napoléon). Yếu tố gen: Đột biến gen ức chế khối u p53.",
        "option_explanations": [
            "Đúng — Đúng từng chi tiết theo barem §1.2: Nhóm máu A có tỷ lệ UTDD cao hơn; gen liên quan là đột biến gen ức chế khối u p53.",
            "Sai — Nhóm máu O thường liên quan đến loét tá tràng lành tính; HER2-neu là đích điều trị thuốc (§6.3) chứ không phải gen ức chế khối u nêu tại §1.2.",
            "Sai — Barem không ghi nhận nhóm máu B có tỷ lệ mắc UTDD cao hơn; gen p53 là gen duy nhất được nêu tên tại §1.2.",
            "Sai — Nhóm máu AB không phải nhóm máu được nêu; nhiễm sắc thể Philadelphia là đặc trưng của bệnh bạch cầu tủy mạn tính, không có trong bài."
        ]
    },
    {
        "id": "SURG21-A10",
        "type": "vignette",
        "topic": "Đại cương & Yếu tố nguy cơ",
        "subtopic": "Tiền sử gia đình và tính chất gia tộc",
        "bloom": "hiểu",
        "difficulty": 2,
        "source": "SURG-21 §1.2",
        "text": "Bệnh nhân nam 48 tuổi đến tư vấn sức khỏe do lo lắng về nguy cơ mắc ung thư dạ dày vì có nhiều người thân trong gia đình cùng mắc bệnh. Giáo trình trích dẫn dẫn chứng lịch sử nào sau đây để minh họa điển hình cho tính chất di truyền gia đình của ung thư dạ dày?",
        "options": [
            "Thống kê của Gauser trên dòng họ 174 người có 41 người mắc và các ghi nhận trong gia tộc Napoléon.",
            "Nghiên cứu phả hệ Hoàng gia Anh ghi nhận đột biến gen quy định tổng hợp chuỗi alpha-fetoprotein.",
            "Thống kê của Billroth trên các gia đình có người thân từng phẫu thuật nối vị tràng sau 10 năm.",
            "Dữ liệu điều tra dịch tễ học tại quần đảo Chilê và Ireland trên các dòng họ công nhân làm muối."
        ],
        "correct": 0,
        "explanation": "Barem §1.2: 'Gia đình có tính chất di truyền (Gauser thống kê dòng họ 174 người có 41 người ung thư dạ dày; gia tộc Napoléon có nhiều người mắc UTDD).'",
        "option_explanations": [
            "Đúng — Khớp chính xác dẫn chứng trong barem §1.2: Gauser thống kê dòng họ 174 người có 41 người mắc ung thư dạ dày, gia tộc Napoléon có nhiều người mắc.",
            "Sai — Hoàng gia Anh và alpha-fetoprotein không có trong bài ung thư dạ dày.",
            "Sai — Billroth là tên phẫu thuật cắt dạ dày, không phải nghiên cứu phả hệ di truyền ung thư trong barem.",
            "Sai — Chilê và Ireland là các quốc gia có tỷ lệ mắc và tử vong có xu hướng giảm nêu tại §1.1, không phải dẫn chứng di truyền gia đình."
        ]
    },
    {
        "id": "SURG21-A11",
        "type": "concept",
        "topic": "Giải phẫu bệnh & Phân giai đoạn TNM",
        "subtopic": "Vị trí giải phẫu khối u dạ dày",
        "bloom": "nhớ",
        "difficulty": 1,
        "source": "SURG-21 §2.1",
        "text": "Theo giải phẫu bệnh học ung thư dạ dày, tỷ lệ phân bố vị trí tổn thương nguyên phát theo các vùng giải phẫu của dạ dày được sắp xếp theo thứ tự tần suất từ cao đến thấp như thế nào?",
        "options": [
            "Vùng hang môn vị (50–60%) > Bờ cong nhỏ (25–30%) > Vùng tâm vị (<10%) > Bờ cong lớn (rất ít gặp).",
            "Bờ cong nhỏ (50–60%) > Vùng hang môn vị (25–30%) > Vùng tâm vị (<10%) > Bờ cong lớn (rất ít gặp).",
            "Vùng hang môn vị (50–60%) > Vùng tâm vị (25–30%) > Bờ cong nhỏ (<10%) > Bờ cong lớn (rất ít gặp).",
            "Vùng tâm vị (50–60%) > Vùng hang môn vị (25–30%) > Bờ cong nhỏ (<10%) > Bờ cong lớn (rất ít gặp)."
        ],
        "correct": 0,
        "explanation": "Barem §2.1: Vùng hang và môn vị: 50–60% (chiếm đa số); Bờ cong nhỏ: 25–30%; Vùng tâm vị: < 10%; Vùng bờ cong lớn: Rất ít gặp.",
        "option_explanations": [
            "Đúng — Phản ánh chính xác tỷ lệ phân bố vị trí giải phẫu khối u trong barem §2.1.",
            "Sai — Bờ cong nhỏ chiếm 25–30%, vùng hang môn vị mới là vị trí chiếm đa số (50–60%) (§2.1).",
            "Sai — Vùng tâm vị chiếm <10%, bờ cong nhỏ chiếm 25–30% (§2.1).",
            "Sai — Vùng tâm vị chiếm <10% chứ không chiếm 50–60% (§2.1)."
        ]
    }
]

with open("F:/DL/mavisresearch/Bai hoc y khoa/16_Ngoai khoa/SURG-21_Ung_thu_da_day/outputs/mcq/part1.json", "w", encoding="utf-8") as f:
    json.dump(part1, f, ensure_ascii=False, indent=2)
print("Part 1 written successfully:", len(part1))
