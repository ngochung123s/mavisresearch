# AGENTS.md — Quy tắc canonical cho `Bai hoc y khoa`

## Evidence provider và build

- Không gọi NCBI/E-utilities trong release workflow; không retry, proxy bypass hoặc hidden fallback.
- Pha online duy nhất cho evidence: `10_Script Python/evidence_sync.py`. Metadata PMID/abstract dùng Europe PMC không lọc Open Access; full text OA là adapter riêng và chỉ dùng khi license phù hợp; Crossref/Retraction Watch, OpenAlex và official-source manifest cung cấp corroboration/provenance.
- Sync phải tạo immutable raw cache, normalized cache và provider-neutral evidence bundle có schema, SHA-256, provenance, thời gian kiểm tra, license và quan hệ official source.
- Pha build bắt buộc offline: mọi verifier và `build_pipeline.py` nhận `--evidence-bundle`. Build chặn network egress trong toàn bộ Python subprocess tree; thiếu/sai/stale bundle là BLOCK.
- Freshness tối đa: metadata/abstract 72 giờ; retraction/correction 24 giờ. Official PDF khóa hash; version/landing metadata phải current.
- Bảy gate tách biệt: existence; exact bibliographic identity; topic relevance; claim–abstract; numeric/full-text; guideline authority/document type; retraction/correction freshness. `pmid_exists=true` không bao giờ đủ để PASS.
- Official-source gate fail-closed: educational material không phải guideline; translation phải lưu `translation_of` và `endorsement_status`; bản dịch không được tổ chức gốc endorse không được gắn official guideline; tài liệu superseded không PASS.

## Research → execute

1. Khóa profile, required gates, `lesson_depth_contract`, output basename và Claim ID trong Research Brief trước khi viết bài.
2. Online sync evidence cho toàn bộ PMID/DOI/official sources. Zero hit Europe PMC chỉ là nonexistence khi query metadata unfiltered trả không có exact record; không dùng OA-zero để kết luận.
3. Chạy `preflight_claim_check.py <brief> --evidence-bundle <bundle> [--topic ...]`; topic screen chỉ đọc bundle offline.
4. Chỉ dùng claim đã khóa trong brief. Claim số liệu phải có population–intervention/comparator–outcome–timepoint và exact quote từ abstract hoặc licensed full text.
5. Chạy canonical `build_pipeline.py --brief ... --lesson ... --cards ... --guidelines ... --evidence-bundle ...`. Citation audit giữ mọi occurrence, không deduplicate, và release yêu cầu 0 BLOCK/0 WARN.
6. Chỉ `PUBLISH READY` mới promote/update catalog.

## Năm nhãn canonical duy nhất

- `[FETCHED]`: metadata đã xác minh; cấm claim định lượng.
- `[ABSTRACT VERIFIED]`: claim định tính khớp abstract.
- `[DATA VERIFIED]`: số liệu khớp exact quote trong abstract hoặc full text thích hợp.
- `[FULL TEXT VERIFIED]`: khớp toàn văn có hash/provenance/license phù hợp.
- `[GUIDELINE VERIFIED]`: recommendation từ official, current, đúng document type, authority/translation/endorsement đã kiểm.

Cấm nhãn cũ `[TEXTBOOK]`, `[ABSTRACT MATCH]`, `[DIRECTION ONLY]`, `[FULL VERIFIED]`; không tự gán nhãn. Kiến thức nền không cần nhãn verification.

## Quy tắc output

- Nội dung tiếng Việt có dấu; thuật ngữ khó dùng `tiếng Việt (English)` ở lần đầu.
- Filename/folder không dấu. Mọi deliverable release nằm trong folder bài học, output nhị phân/evidence trong `outputs/`.
- Bài mới dùng `L3_BEGINNER`, dạy từ gốc; bài cấp cứu có BOX ĐỎ và Plan B.
- Không ghi ổ C; không sửa/release bài học trong cùng workstream sửa verifier.
