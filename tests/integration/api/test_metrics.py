from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from icon_metrics.config import settings


def test_api_get_supply(db: Session, client: TestClient):
    response = client.get(f"{settings.REST_PREFIX}/metrics/supply")
    assert response.status_code == 200
