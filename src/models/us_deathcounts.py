from sqlmodel import SQLModel, Field, Column
from sqlalchemy import String, Integer, Date
from typing import Optional
from datetime import date

class USDeathCounts(SQLModel, table=True):
    __tablename__ = "CLN_US_DEATHCOUNTS"

    id: int = Field(sa_column=Column("id", Integer, primary_key=True, quote=True))
    year: int = Field(sa_column=Column("year", Integer, quote=True))
    month: int = Field(sa_column=Column("month", Integer, quote=True))
    group: str = Field(sa_column=Column("group", String, quote=True))
    subgroup1: Optional[str] = Field(sa_column=Column("subgroup1", String, quote=True))
    subgroup2: Optional[str] = Field(sa_column=Column("subgroup2", String, quote=True))
    covid_deaths: Optional[int] = Field(sa_column=Column("covid_deaths", Integer, quote=True))
    crude_covid_death_rate: Optional[int] = Field(sa_column=Column("crude_covid_death_rate", Integer, quote=True))
    age_adjusted_covid_death_rate: Optional[int] = Field(sa_column=Column("age_adjusted_covid_death_rate", Integer, quote=True))
    annualized_crude_covid_death_rate: Optional[int] = Field(sa_column=Column("annualized_crude_covid_death_rate", Integer, quote=True))
    annualized_age_adjusted_covid_death_rate: Optional[int] = Field(sa_column=Column("annualized_age_adjusted_covid_death_rate", Integer, quote=True))
    footnote: Optional[str] = Field(sa_column=Column("footnote", String, quote=True))
    LAST_UPDATED: date = Field(sa_column=Column("LAST_UPDATED", Date, quote=True))
