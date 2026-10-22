# Quy tắc cho agent — dự án ngayhoi

## Dự án
Cổng đăng ký Ngày hội việc làm. FastAPI + SQLite, mã máy chủ ở `main.py`.
Đặc tả trong `spec.md`. Chạy test: `python -m pytest -q` ở thư mục gốc.

## Phạm vi
- Mỗi PR làm **một việc**, **dưới 200 dòng**.
- Chỉ sửa tệp được nêu trong câu giao việc; tệp test mới đặt trong `tests/`.

## Không được sửa
- `tests/test_gioi_han.py` và mọi test đã có — đó là test của người.
- `.github/` (CI và mẫu PR).
- `frontend/`, `evidence/`, `spec.md` (trừ khi được giao).

## Quy trình
1. Viết test cho tính năng mới **trước**, chạy thấy đỏ đúng lý do.
2. Viết mã cho đến khi **toàn bộ** test xanh, rồi **dừng**.
3. Không tự hợp nhất. Mở PR theo mẫu năm mục: Việc · Vì sao · Bằng chứng · Phần AI làm · Cần soi kỹ.

## Hợp nhất
Nhóm dùng **Merge commit** để giữ riêng commit test và commit mã trên `master`.
