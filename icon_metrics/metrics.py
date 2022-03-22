from prometheus_client import Counter, Gauge


class Metrics:
    circulating_supply = Gauge("circulating_supply", "Total supply - org supply.")
    organization_supply = Gauge("organization_supply", "All org wallet balances.")
    total_supply = Gauge("total_supply", "Total supply.")
    supply_cron_ran = Counter("preps_base_cron_ran", "")


prom_metrics = Metrics()
