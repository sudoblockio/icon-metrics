from time import sleep

from sqlalchemy.orm import sessionmaker
from sqlmodel import select

from icon_metrics.config import settings
from icon_metrics.db import engine
from icon_metrics.log import logger
from icon_metrics.metrics import Metrics
from icon_metrics.models.addresses import Address
from icon_metrics.models.metrics import Supply
from icon_metrics.utils.rpc import getBalance, getTotalSupply

metrics = Metrics()


def calculate_organization_supply(addresses):
    organization_supply = 0

    for address in addresses:
        address_balance = int(getBalance(address), 16)
        organization_supply += address_balance

    return organization_supply


def supply_cron_worker():
    """Cron job to scrape a list of known address balances and sum them to get the total supply."""
    SessionMade = sessionmaker(bind=engine)
    session = SessionMade()

    i = 0
    addresses = []
    while True:

        supply = Supply()
        supply.total_supply = int(getTotalSupply(), 16)

        if i % 100 == 0:
            # Wait 100 iterations to refresh
            query = select(Address).where(Address.organization_wallet)
            result = session.execute(query)
            addresses = result.scalars().all()
            logger.info(f"Iteration {i}")

        supply.organization_supply = calculate_organization_supply([i.address for i in addresses])

        supply.circulating_supply = supply.total_supply - supply.organization_supply

        session.add(supply)
        session.commit()

        metrics.organization_supply = supply.organization_supply
        metrics.circulating_supply = supply.circulating_supply
        metrics.total_supply = supply.total_supply
        sleep(settings.CRON_SLEEP_SEC)
        i += 1


if __name__ == "__main__":
    supply_cron_worker()
