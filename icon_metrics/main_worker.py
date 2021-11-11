import asyncio
from multiprocessing.pool import ThreadPool
from threading import Thread

from loguru import logger
from prometheus_client import start_http_server
from sqlalchemy.orm import scoped_session

from icon_metrics.config import settings
from icon_metrics.workers.db import session_factory
from icon_metrics.workers.supply_cron import supply_cron_worker

logger.info("Starting metrics server.")
metrics_pool = ThreadPool(1)
metrics_pool.apply_async(start_http_server, (settings.METRICS_PORT, settings.METRICS_ADDRESS))

Session = scoped_session(session_factory)

supply_cron_session = Session()

supply_cron_worker_thread = Thread(
    target=supply_cron_worker,
    args=(supply_cron_session,),
)

supply_cron_worker_thread.start()
supply_cron_worker_thread.join()
