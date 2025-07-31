from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.ca_antibody import CAAntibody
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine

def fetch_ca_antibody():
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        stmt = select(CAAntibody)
        results = session.execute(stmt).scalars().all()
        ca_antibody_list = [row.model_dump() for row in results]
    return ca_antibody_list
