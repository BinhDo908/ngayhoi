import os
import sys
import tempfile
from pathlib import Path

# CSDL tạm, đặt TRƯỚC khi import main.
os.environ.setdefault("DB_PATH", os.path.join(tempfile.mkdtemp(), "test.db"))
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


def con_cho(ma_phien):
    return client.get("/api/con-cho", params={"ma_phien": ma_phien})


def test_phien_trong_con_du_30_cho():
    r = con_cho("P01")
    assert r.status_code == 200
    assert r.json() == {"con_cho": 30}


def test_phien_co_29_con_1_cho():
    lap_day("P01", 29)
    assert con_cho("P01").json() == {"con_cho": 1}


def test_phien_day_con_0_cho():
    lap_day("P01", 30)
    assert con_cho("P01").json() == {"con_cho": 0}


def test_dem_rieng_tung_phien():
    lap_day("P01", 30)
    assert con_cho("P02").json() == {"con_cho": 30}


def test_thieu_ma_phien_bao_422():
    assert client.get("/api/con-cho").status_code == 422
