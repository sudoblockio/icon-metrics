from time import sleep

from requests import get, post

from icon_metrics.config import settings
from icon_metrics.metrics import Metrics

metrics = Metrics()


def prometheus_cron_worker():
    if settings.MAIN_PROMETHEUS_ENDPOINT:
        return

    while True:
        r = get(settings.MAIN_PROMETHEUS_ENDPOINT)
        sleep(settings.CRON_SLEEP_SEC)
