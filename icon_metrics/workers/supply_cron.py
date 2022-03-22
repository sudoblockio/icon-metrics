import csv
import os
from datetime import datetime

from icon_metrics.models.metrics import Supply
from icon_metrics.utils.rpc import getBalance, getStake, getTotalSupply

BURN_ADDRESS = "hx1000000000000000000000000000000000000000"


def get_organization_addresses() -> list:
    addresses = []
    path = os.path.join(os.path.dirname(__file__), "organization-addresses.csv")
    with open(path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            addresses.append(row[0])
    return addresses


def calculate_organization_supply():
    organization_supply = 0
    addresses = get_organization_addresses()
    for address in addresses:
        address_balance = int(getBalance(address), 16)

        stakes = getStake(address)
        address_balance += int(stakes["stake"], 16)
        for i in stakes["unstakes"]:
            address_balance += int(i["unstake"], 16)
        organization_supply += address_balance

    return organization_supply


def get_supply(session):
    supply = Supply()
    supply.timestamp = datetime.now().timestamp()
    supply.total_supply = int(getTotalSupply(), 16)
    supply.organization_supply = calculate_organization_supply()
    supply.circulating_supply = supply.total_supply - int(getBalance(BURN_ADDRESS), 16)

    session.merge(supply)
    session.commit()
