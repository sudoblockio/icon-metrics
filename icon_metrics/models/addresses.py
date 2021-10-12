from typing import Optional

from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel


class Address(SQLModel, table=True):
    """Internal table to find lists of addresses to monitor."""

    address: Optional[str] = Field(None, primary_key=True)
    organization_wallet: Optional[bool] = Field(False, index=True)

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        return "addresses"
