from datetime import datetime
from time import sleep

from sqlmodel import select

from icon_metrics.config import settings
from icon_metrics.log import logger
from icon_metrics.metrics import Metrics
from icon_metrics.models.addresses import Address
from icon_metrics.models.metrics import Supply
from icon_metrics.utils.rpc import getBalance, getStake, getTotalSupply

metrics = Metrics()


def calculate_organization_supply(addresses):
    organization_supply = 0

    for address in addresses:
        address_balance = int(getBalance(address), 16)

        address_balance += int(getStake(address)["stake"], 16)
        organization_supply += address_balance

    return organization_supply


def get_supply(session, iteration: int):
    addresses = []

    supply = Supply()
    supply.total_supply = int(getTotalSupply(), 16)
    supply.timestamp = datetime.now().timestamp()

    if iteration % 100 == 0:
        # Wait 100 iterations to refresh
        query = select(Address).where(Address.organization_wallet)
        result = session.execute(query)
        addresses = result.scalars().all()

    supply.organization_supply = calculate_organization_supply([i.address for i in addresses])

    supply.circulating_supply = supply.total_supply - supply.organization_supply

    session.merge(supply)
    session.commit()


def supply_cron_worker(session):
    """Cron job to scrape a list of known address balances and sum them to get the total supply."""

    iteration = 0
    while True:
        logger.info(f"Iteration {iteration}")
        get_supply(session, iteration)
        sleep(settings.CRON_SLEEP_SEC)
        iteration += 1


if __name__ == "__main__":
    from icon_metrics.workers.db import session_factory

    with session_factory() as session:
        supply_cron_worker(session)
