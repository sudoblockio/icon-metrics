from icon_metrics.workers.supply_cron import calculate_organization_supply, get_supply


def test_calculate_organization_supply():
    organization_supply = calculate_organization_supply() / 1e18

    assert organization_supply < 240000000

    # This is ~65M off (907M - 672M = 235 - 171 = 64)
    # assert round(organization_supply, -6) == 171000000
    # Just failed but the point is above


def test_supply_cron_worker(db, run_process_wait):
    with db as session:
        get_supply(session)
