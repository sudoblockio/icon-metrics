# from time import sleep
#
# from requests import get, post
#
# from icon_metrics.config import settings
# from icon_metrics.metrics import Metrics
#
# metrics = Metrics()
#
#
# def prometheus_cron_worker():
#     if settings.MAIN_PROMETHEUS_ENDPOINT:
#         return
#
#     while True:
#         r = get(settings.MAIN_PROMETHEUS_ENDPOINT)
#         sleep(settings.CRON_SLEEP_SEC)
#
# def prep_status_cron_worker():
#
#     while True:
#         logger.info("")
#         preps = post_rpc_json(getPReps())
#
#         if preps is None:
#             logger.info("No preps found from rpc. Chilling for a bit.")
#             sleep(60)
#             continue
#
#         prep_status = get_prep_status()
#
#         for p in preps["preps"]:
#             prep = session.get(Prep, p["address"])
#             if prep is None:
#                 logger.info("No preps found in db? Should not ever happen cuz of db_init.")
#                 continue
#
#             prep.node_status = ""
#
#         logger.info("Cron ran.")
#         sleep(settings.CRON_SLEEP_SEC)
