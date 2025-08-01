from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlmodel import Column, Field, SQLModel


class DATASET_METADATA(SQLModel, table=True):
    __tablename__ = "CLN_DATASET_METADATA"

    DATASET_ID: int = Field(sa_column=Column("DATASET_ID", Integer, primary_key=True))
    COUNTRY: str = Field(sa_column=Column("COUNTRY", String, quote=True))
    DATASET_NAME: str = Field(sa_column=Column("DATASET_NAME", String, quote=True))
    DESCRIPTION: str = Field(sa_column=Column("DESCRIPTION", String, quote=True))
    LAST_UPDATED: datetime = Field(
        sa_column=Column("LAST_UPDATED", DateTime, quote=True)
    )
