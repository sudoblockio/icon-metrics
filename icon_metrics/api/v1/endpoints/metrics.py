from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from icon_metrics.db import get_session
from icon_metrics.models.metrics import Supply

router = APIRouter()


@router.get("/metrics/supply")
async def get_supply(session: AsyncSession = Depends(get_session)) -> Supply:
    """Get latest supply."""
    result = await session.execute(select(Supply))
    preps = result.first()
    return preps
