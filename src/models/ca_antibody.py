from sqlmodel import SQLModel, Field, Column
from sqlalchemy import String, Float, Date, DateTime, Integer
from datetime import date, datetime
from typing import Optional

class CAAntibody(SQLModel, table=True):
    __tablename__ = "CLN_CA_ANTIBODY"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, quote=True))
    REF_DATE: date = Field(sa_column=Column("REF_DATE", Date, quote=True))
    DGUID: str = Field(sa_column=Column("DGUID", String, quote=True))
    Measure: str = Field(sa_column=Column("Measure", String, quote=True))
    Sex_at_birth: str = Field(sa_column=Column("Sex at birth", String, quote=True))
    Age_group: str = Field(sa_column=Column("Age group", String, quote=True))
    Characteristics: str = Field(sa_column=Column("Characteristics", String, quote=True))
    VECTOR: str = Field(sa_column=Column("VECTOR", String, quote=True))
    COORDINATE: str = Field(sa_column=Column("COORDINATE", String, quote=True))
    PERCENT: Optional[float] = Field(sa_column=Column("PERCENT", Float, quote=True))
    DATA_QUALITY_RATING: Optional[str] = Field(sa_column=Column("DATA_QUALITY_RATING", String, quote=True))
    LAST_UPDATED: datetime = Field(sa_column=Column("LAST_UPDATED", DateTime, quote=True))
