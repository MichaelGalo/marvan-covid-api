from sqlmodel import SQLModel, Field, Column, Integer
from sqlalchemy import String, Float, Date, DateTime
from datetime import date, datetime
from typing import Optional

class CARapidTestDemand(SQLModel, table=True):
    __tablename__ = "CLN_CA_RAPIDTESTDEMAND"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, quote=True))
    REF_DATE: date = Field(sa_column=Column("REF_DATE", Date, quote=True))
    DGUID: str = Field(sa_column=Column("DGUID", String, quote=True))
    NAICS: str = Field(sa_column=Column("North American Industry Classification System (NAICS)", String, quote=True))
    RapidTestDemandUsage: str = Field(sa_column=Column("COVID-19 rapid test kits demand and usage", String, quote=True))
    VECTOR: str = Field(sa_column=Column("VECTOR", String, quote=True))
    COORDINATE: str = Field(sa_column=Column("COORDINATE", String, quote=True))
    PERCENT: Optional[float] = Field(sa_column=Column("PERCENT", Float, quote=True))
    DATA_QUALITY_RATING: Optional[str] = Field(sa_column=Column("DATA_QUALITY_RATING", String, quote=True))
    LAST_UPDATED: datetime = Field(sa_column=Column("LAST_UPDATED", DateTime, quote=True))
