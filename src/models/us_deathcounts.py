
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

#FIXME: Requires a primary key
class USDeathCounts(SQLModel, table=True):
    __tablename__ = "CLN_US_DEATHCOUNTS"
    id: int = Field(primary_key=True)
    year: int = Field()
    month: int = Field()
    group: str = Field()
    subgroup1: Optional[str] = Field()
    subgroup2: Optional[str] = Field()
    covid_deaths: Optional[int] = Field()
    crude_covid_death_rate: Optional[int] = Field()
    age_adjusted_covid_death_rate: Optional[int] = Field()
    annualized_crude_covid_death_rate: Optional[int] = Field()
    annualized_age_adjusted_covid_death_rate: Optional[int] = Field()
    footnote: Optional[str] = Field()
    LAST_UPDATED: Optional[date] = Field()