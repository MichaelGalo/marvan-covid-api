from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.uk_cases_by_day import UKCovCasesByDay
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine

def fetch_uk_cases_by_day():
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        stmt = select(UKCovCasesByDay)
        results = session.execute(stmt).scalars().all()
        uk_cases_list = [case.model_dump() for case in results]
    return uk_cases_list