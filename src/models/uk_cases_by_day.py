from sqlmodel import SQLModel, Field, Column
from sqlalchemy import Integer, Date
from typing import Optional
from datetime import date, datetime

class UKCovCasesByDay(SQLModel, table=True):
    __tablename__ = "CLN_UK_COVCASESBYDAY"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, quote=True))
    report_date: date = Field(sa_column=Column("date", Date, quote=True))  # renamed field due to pydantic errors, column stays "date"
    epiweek: Optional[int] = Field(sa_column=Column("epiweek", Integer, quote=True))
    daily_case_count: Optional[int] = Field(sa_column=Column("daily_case_count", Integer, quote=True))
    LAST_UPDATED: date = Field(sa_column=Column("LAST_UPDATED", Date, quote=True))