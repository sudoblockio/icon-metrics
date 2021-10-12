from prometheus_client import Gauge


class Metrics:
    def __init__(self):
        self.circulating_supply = Gauge("circulating_supply", "Total supply - org supply.")

        self.organization_supply = Gauge("organization_supply", "All org wallet balances.")

        self.total_supply = Gauge("total_supply", "Total supply.")
