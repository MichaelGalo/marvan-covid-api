from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.ca_rapidtestdemand import CARapidTestDemand
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine

def fetch_ca_rapidtestdemand():
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        stmt = select(CARapidTestDemand)
        results = session.execute(stmt).scalars().all()
        ca_rapidtestdemand_list = [row.model_dump() for row in results]
    return ca_rapidtestdemand_list
