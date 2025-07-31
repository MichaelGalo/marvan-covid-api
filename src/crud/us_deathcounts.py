from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.us_deathcounts import USDeathCounts
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine


def fetch_us_deathcounts():
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        stmt = select(USDeathCounts)
        results = session.execute(stmt).scalars().all()
        # Convert model instances to dicts for FastAPI serialization
        us_deathcounts_list = [weather.model_dump() for weather in results]
    return us_deathcounts_list