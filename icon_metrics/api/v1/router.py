from fastapi import APIRouter

from icon_metrics.api.v1.endpoints import metrics

api_router = APIRouter()
api_router.include_router(metrics.router)
