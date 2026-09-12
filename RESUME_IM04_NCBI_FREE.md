# RESUME — IM-04 và migration build không NCBI

> Ngày bàn giao: 2026-07-29
> Working directory: `F:/DL/mavisresearch`
> Trạng thái: IM-04 đang BLOCK release; bước tiếp theo là workstream độc lập migrate toolchain không NCBI.

## 1. Việc cần làm khi mở terminal mới

1. Đọc `AGENTS.md`, `Bai hoc y khoa/WORKFLOW.md`, và file này.
2. Khởi tạo todo cho workstream độc lập `NCBI-free evidence provider`.
3. KHÔNG tiếp tục viết/release IM-04 trước khi migration hoàn tất và regression tests PASS.
4. Sau clean cutover, quay lại IM-04 theo thứ tự Research Brief → strict gates → Markdown → cards → build pipeline → PUBLISH READY.

## 2. Mục tiêu người dùng

Xây chuyên đề `IM-04 — Hướng dẫn đọc xét nghiệm máu cơ bản`, gồm 3 Part trong cùng folder, đồng thời thay toolchain để mọi build sau không gọi NCBI/E-utilities và không phụ thuộc mạng trong lúc build.

Folder:
`Bai hoc y khoa/11_Noi khoa/IM-04_Huong_dan_doc_xet_nghiem_mau_co_ban/`

Basenames đã khóa:
- `IM-04_Part1_Nguyen_ly_doc_xet_nghiem_2026-07-29_RELEASE_v1`
- `IM-04_Part2_Huyet_hoc_va_dong_mau_2026-07-29_RELEASE_v1`
- `IM-04_Part3_Sinh_hoa_va_tich_hop_2026-07-29_RELEASE_v1`

Profile: `foundation`; mode: `L3_BEGINNER`; exact 16 gates/depth contract nằm trong `IM-04_RELEASE_PLAN.md`.

## 3. Quy tắc cứng

- Không ghi file vào ổ C; output dự án nằm trong `F:/DL/mavisresearch`.
- Nội dung tiếng Việt có dấu; filename/folder không dấu.
- Fail-closed; không tự gán nhãn.
- Năm nhãn canonical duy nhất: `[FETCHED]`, `[ABSTRACT VERIFIED]`, `[DATA VERIFIED]`, `[FULL TEXT VERIFIED]`, `[GUIDELINE VERIFIED]`.
- Không sửa verifier trong cùng workstream release IM-04. Migration provider là workstream độc lập.
- Không viết bài trước Research Brief đã khóa và strict preflight PASS.
- Chỉ cập nhật README/catalog sau `PUBLISH READY`.

## 4. Artifact hiện có

Trong folder IM-04:
- `IM-04_RELEASE_PLAN.md`
- `IM-04_PART1_SOURCE_RESEARCH.md`
- `IM-04_PART1_OFFICIAL_SOURCE_INVENTORY.md`
- `IM-04_PART1_EFLM_QUOTE_CANDIDATES.md`
- `IM-04_PART2_PART3_SOURCE_MAP.md`
- `IM-04_PART2_PART3_OFFICIAL_SOURCE_INVENTORY.md`
- `IM-04_PART2_BSH_QUOTE_CANDIDATES.md`
- `IM-04_PART3_KDIGO_QUOTE_CANDIDATES.md`
- `outputs/verification/provider_probe/EUROPE_PMC_PROVIDER_PROBE.md`
- `outputs/verification/provider_probe/EUROPE_PMC_PROVIDER_PROBE.json`

Local source chính:
- Part 1 EFLM 2018: `outputs/sources/part1/eflm_colabiocli_venous_blood_sampling_2018.pdf`; SHA-256 `3deff217dc1a704aa83fbced7e424f7c7be8eec64dff698339a61d74c16524e7`.
- Part 1 survey 2024: `outputs/sources/part1/eflm_colabiocli_survey_lithuania_2024.pdf`; SHA-256 `176e4a3c35121cbc454b55419b56ea3c2f27c157171a3eca39d425b9a4551e85`.
- Part 2 BSH FBC: `outputs/sources/part2/BSH_FBC_2022_Educational_Guide.pdf`; SHA-256 `3e247179ae29a4b627f9d6828434e27a30a30c3621c3391d5646ce5ee78906a4`.
- Part 2 BSH clotting: `outputs/sources/part2/BSH_Clotting_Screen_2022_Educational_Guide.pdf`; SHA-256 `09a53d8d07d4710609492b9ae8c927dd19304db65698ce3f32ba0d69f90b281e`.
- Part 3 KDIGO: `outputs/sources/part3/KDIGO_2012_AKI_Guideline.pdf`; SHA-256 `20db2b44ea228cd1006ea9f867ee8d830663fae04c7f1ac3d24aaab7388ed1ad`.

## 5. Phát hiện quan trọng

- IP truy cập NCBI đã bị tạm block; direct E-utilities đã dừng. Không retry, không dùng proxy né block, không yêu cầu NCBI API key để tiếp tục kiến trúc mới.
- PMID `29910186` thực tế là bài `Structural Basis of Phosphatidic Acid Sensing by APH in Apicomplexan Parasites`, không phải EFLM venous sampling. Đây là regression fixture bắt buộc: PMID tồn tại nhưng sai bài/topic phải BLOCK.
- PMID `27235445` trả zero qua Europe PMC wrapper hiện tại vì wrapper ép `OPEN_ACCESS:y`; zero OA không chứng minh PMID không tồn tại.
- Các candidate hiện tại không được grandfather thành verified.
- BSH 2022 là educational resources, không phải formal guideline.

## 6. Audit phụ thuộc NCBI

Các script hiện gọi NCBI trực tiếp hoặc phụ thuộc logic NCBI:
- `preflight_check_pmids.py`
- `verify_all_pmids.py`
- `verify_claims.py`
- `verify_claim_vs_abstract.py`
- `retraction_check.py`
- `citation_audit.py`
- `build_pipeline.py` gọi các verifier trên qua subprocess.

Cache hiện rời rạc, không immutable, thiếu provider provenance/hash/freshness thống nhất. Không thêm fallback chắp vá; cần clean cutover.

## 7. Kiến trúc đã chốt

```text
ONLINE EVIDENCE SYNC
  Europe PMC metadata adapter, không ép Open Access
  + Europe PMC OA full-text adapter riêng
  + Crossref / Retraction Watch
  + OpenAlex corroboration
  + official society guideline sources
        ↓
  provider-neutral evidence bundle
  raw immutable cache + normalized cache
  hashes + provenance + TTL + license
        ↓
OFFLINE BUILD
  build_pipeline.py --evidence-bundle
  network disabled
  schema/hash/freshness/gate verification
        ↓
  DOCX + APKG + learner artifacts + publish gate
```

NCBI disabled/default absent; không hidden fallback; không proxy bypass.

Gate phải tách:
1. Existence.
2. Exact bibliographic identity.
3. Topic relevance.
4. Claim-to-abstract match.
5. Numeric/full-text verification.
6. Guideline authority/document type.
7. Fresh retraction/correction status.

Freshness:
- Metadata/abstract refresh trong 72 giờ trước publish.
- Retraction/correction không quá 24 giờ.
- Official PDF khóa immutable hash; landing page/version kiểm freshness.

## 8. Workstream tiếp theo: migration độc lập

Đề xuất module:
- `evidence_sync.py`
- provider adapters: Europe PMC metadata, Europe PMC OA, Crossref/Retraction Watch, OpenAlex, official source.
- provider-neutral bundle schema.
- immutable raw cache và normalized cache.
- offline verifiers.
- network-egress guard trong build/test.

Clean cutover mọi callsite của các script audit ở mục 6; xóa network logic NCBI cũ, không shim/alias.

Regression corpus tối thiểu:
1. `29910186`: valid PMID, wrong Apicomplexa topic.
2. `27235445`: OA zero != nonexistent.
3. Valid exact match.
4. Nonexistent PMID.
5. Missing abstract.
6. Title mismatch.
7. PMID–DOI conflict.
8. Retracted article.
9. Expression of concern.
10. Correction affects claim.
11. Correction does not affect claim but needs adjudication.
12. Reinstatement.
13. Guideline without PMID.
14. Educational slide mislabeled guideline.
15. Raw hash mismatch.
16. Stale retraction artifact.
17. HTTP 429.
18. HTTP 5xx/malformed/provider outage.
19. Non-OA metadata record.
20. PMCID/full text without suitable reuse license.
21. Provider conflict.
22. Build attempts E-utilities/network egress.

Invariant: không PASS chỉ vì `pmid_exists=true`.

Rollout:
1. Spec/schema.
2. Adapters/cache/evidence sync.
3. Offline gates + tests.
4. Shadow mode trên release cũ.
5. Egress audit chứng minh build không gọi mạng/NCBI.
6. Clean default cutover.
7. Quay lại IM-04.

## 9. Trạng thái

### DONE
- Khóa folder/basenames/profile/depth contract IM-04.
- Lập source maps/inventories.
- Lưu local EFLM, BSH, KDIGO và quote candidates.
- Probe Europe PMC và phát hiện PMID mismatch.
- Audit phạm vi phụ thuộc NCBI.
- Chốt kiến trúc NCBI-free, build offline.

### BLOCKED
- Research Brief, lesson, cards và release của cả 3 Part.
- README/catalog update.

### NEXT
- Implement và verify workstream provider-neutral không NCBI.
- Sau cutover mới resume IM-04 Part 1 → Part 2 → Part 3.

## 10. Tuyệt đối không làm

- Không retry hoặc crawl NCBI.
- Không dùng proxy/VPN để né block.
- Không dùng Europe PMC OA wrapper để kết luận PMID không tồn tại.
- Không coi PMID tồn tại là đủ.
- Không gắn BSH educational resources thành guideline.
- Không gán nhãn verification khi chưa có gate artifact.
- Không viết lesson/cards trước strict Brief PASS.
- Không sửa verifier và release IM-04 trong cùng workstream.
- Không cập nhật README/catalog trước PUBLISH READY.

## 11. Prompt để dán vào terminal mới

```text
Đọc `F:/DL/mavisresearch/RESUME_IM04_NCBI_FREE.md`, sau đó đọc `AGENTS.md`, `Bai hoc y khoa/WORKFLOW.md`, skills medical verification/release gates và các file được dẫn trong handoff. Khởi tạo todo đầy đủ. Bắt đầu workstream độc lập migrate toolchain sang provider-neutral NCBI-free với hai pha: online `evidence_sync.py` tạo hashed evidence bundle và offline `build_pipeline.py --evidence-bundle` cấm network. Không sửa/release IM-04 trong cùng workstream. Implement adapters/cache/schema/gates, migration toàn bộ callsites, regression corpus gồm 29910186 và 27235445, shadow tests và egress test. Chỉ sau clean cutover + full tests PASS mới quay lại build ba Part IM-04 theo workflow fail-closed.
```

`--resume` một mình không đủ; hãy dùng prompt trên hoặc nói: `Đọc RESUME_IM04_NCBI_FREE.md và tiếp tục đầy đủ`.
