import os
import sys
import tempfile
from pathlib import Path

# CSDL tạm, không đụng dữ liệu thật. Phải đặt TRƯỚC khi import main.
# Dùng tệp tạm thay vì ":memory:" vì main.py mở kết nối mới cho mỗi yêu cầu.
os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "test.db")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import sqlite3
import pytest
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def so_trong():
    main.khoi_tao_co_so_du_lieu()
    with sqlite3.connect(main.DATABASE_PATH) as db:
        db.execute("DELETE FROM dang_ky")


def lap_day(ma_phien, n):
    for i in range(n):
        client.post("/api/dang-ky", json={"ma_sv": f"SV{i:03}", "ma_phien": ma_phien})


def dang_ky(ma_sv, ma_phien):
    return client.post("/api/dang-ky", json={"ma_sv": ma_sv, "ma_phien": ma_phien})


def test_dong1_phien_trong_dang_ky_duoc():
    assert dang_ky("SV001", "P01").status_code == 201


def test_dong2_phien_co_29_van_con_cho():
    lap_day("P01", 29)
    assert dang_ky("SV999", "P01").status_code == 201


def test_dong3_phien_du_30_thi_het_cho():
    lap_day("P01", 30)
    r = dang_ky("SV999", "P01")
    assert r.status_code == 409
    assert r.json()["detail"] == "HET_CHO"


def test_dong4_da_dang_ky_roi_bao_da_dang_ky():
    lap_day("P01", 30)
    r = dang_ky("SV000", "P01")
    assert r.status_code == 409
    assert r.json()["detail"] == "DA_DANG_KY"


def test_dong5_dem_rieng_tung_phien():
    lap_day("P01", 30)
    assert dang_ky("SV031", "P02").status_code == 201
