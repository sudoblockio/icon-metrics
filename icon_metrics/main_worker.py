from time import sleep

from loguru import logger
from prometheus_client import start_http_server

from icon_metrics.config import settings
from icon_metrics.metrics import prom_metrics
from icon_metrics.workers.db import session_factory
from icon_metrics.workers.supply_cron import get_supply


def main():
    logger.info("Starting metrics server.")
    start_http_server(settings.METRICS_PORT, settings.METRICS_ADDRESS)

    while True:
        with session_factory() as session:
            logger.info("Starting cron")

            # Supply
            get_supply(session)
            prom_metrics.supply_cron_ran.inc()

            # Sleep
            sleep(settings.CRON_SLEEP_SEC)


if __name__ == "__main__":
    main()
