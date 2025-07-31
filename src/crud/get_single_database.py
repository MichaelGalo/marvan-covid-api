from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.us_deathcounts import USDeathCounts
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine
from src.models.ca_antibody import CAAntibody
from src.models.ca_rapidtestdemand import CARapidTestDemand
from src.models.uk_cases_by_day import UKCovCasesByDay
from src.dependencies.logger_init import setup_logging
logger = setup_logging()

def fetch_single_database(database_id, offset, limit):
    logger.info(f"Fetching single database with ID: {database_id}, offset: {offset}, limit: {limit}")
    MODEL = None
    if database_id == 1:
        MODEL = CAAntibody
        logger.debug("Using CAAntibody model")
    elif database_id == 2:
        MODEL = CARapidTestDemand
        logger.debug("Using CARapidTestDemand model")
    elif database_id == 3:
        MODEL = UKCovCasesByDay
        logger.debug("Using UKCovCasesByDay model")
    elif database_id == 4:
        MODEL = USDeathCounts
        logger.debug("Using USDeathCounts model")
    elif database_id == None:
        logger.error("Database ID is None")
        raise ValueError("Database ID cannot be None")
    else:
        raise ValueError("Invalid database_id provided.")
    
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        logger.info(f"Executing query for model: {MODEL.__name__} with offset: {offset} and limit: {limit}")
        stmt = select(MODEL).offset(offset).limit(limit)
        results = session.execute(stmt).scalars().all()
        logger.info(f"Query executed successfully, found {len(results)} records")
        single_database = [record.model_dump() for record in results]
    return single_database