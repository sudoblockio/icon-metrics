import csv

import pytest

from icon_metrics.workers.supply_cron import calculate_organization_supply


@pytest.fixture()
def organization_addresses(data_dir):
    addresses = []
    with open(data_dir) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            addresses.append(row[0])
    return addresses


def test_calculate_organization_supply(organization_addresses):
    organization_supply = calculate_organization_supply(organization_addresses) / 1e18

    assert organization_supply < 240000000

    # This is ~65M off (907M - 672M = 235 - 170 = 65)
    assert round(organization_supply) == 170535822
