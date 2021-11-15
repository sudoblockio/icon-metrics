from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Transactions(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    timestamp: Optional[int] = Field(datetime.now().timestamp(), index=True)
    total_tx: Optional[int] = Field(None, index=False)


class Supply(SQLModel, table=True):
    id: Optional[int] = Field(None, primary_key=True)
    timestamp: Optional[int] = Field(None, index=True)
    total_supply: Optional[float] = Field(0, index=False)
    organization_supply: Optional[float] = Field(0, index=False)
    circulating_supply: Optional[float] = Field(0, index=False)


class NodeState(BaseModel):
    prep_name: str
    state_id: int
