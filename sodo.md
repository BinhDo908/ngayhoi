# Sơ đồ hoạt động

```text
Giao diện React (http://localhost:5173)
              |
              | POST /api/dang-ky
              v
FastAPI (http://localhost:8000)
              |
              v
SQLite dangky.db
              |
              +-- Dữ liệu mới: 201 {"ok": true}
              +-- Trùng ma_sv, ma_phien: 409 {"detail": "DA_DANG_KY"}
              +-- Thiếu hoặc sai dữ liệu: 422
```
