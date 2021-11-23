from sqlmodel import select

from icon_metrics.models.metrics import Supply
from icon_metrics.workers.supply_cron import get_supply


def test_get_supply(db):
    with db as session:
        get_supply(session, 0)
        result = session.execute(select(Supply))
        supply = result.scalars().all()
        assert len(supply) >= 1
        assert supply[-1].timestamp > 100000
