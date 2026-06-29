import sys
from pathlib import Path

# Añadimos la raíz del proyecto al PYTHONPATH (clave en CI/CD)
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import app


def test_root():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200