from sqlalchemy import select
from enum import Enum
from sqlalchemy.orm import Session

from src.dependencies.logger_init import setup_logging
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine
from src.models.ca_antibody import CAAntibody
from src.models.ca_rapidtestdemand import CARapidTestDemand
from src.models.uk_cases_by_day import UKCovCasesByDay
from src.models.us_deathcounts import USDeathCounts
from src.models.dataset_metadata import DATASET_METADATA

logger = setup_logging()

class DatasetModel(Enum):
    DATASET_METADATA = 0
    CA_ANTIBODY = 1
    CA_RAPID_TEST_DEMAND = 2
    UK_COV_CASES_BY_DAY = 3
    US_DEATH_COUNTS = 4

model_map = {
    DatasetModel.DATASET_METADATA: DATASET_METADATA,
    DatasetModel.CA_ANTIBODY: CAAntibody,
    DatasetModel.CA_RAPID_TEST_DEMAND: CARapidTestDemand,
    DatasetModel.UK_COV_CASES_BY_DAY: UKCovCasesByDay,
    DatasetModel.US_DEATH_COUNTS: USDeathCounts,
}

def fetch_single_dataset(dataset_id, offset, limit):
    logger.info(f"Fetching single dataset with ID: {dataset_id}, offset: {offset}, limit: {limit}")
    try:
        db_model = DatasetModel(dataset_id)
    except ValueError:
        logger.info("dataset_id not valid.")
        raise ValueError("Invalid dataset_id provided.")
    MODEL = model_map.get(db_model)
    if MODEL is None:
        logger.error("Unhandled dataset_id")
        raise ValueError("Unhandled dataset_id")
    logger.info(f"Using {MODEL.__name__} model")
    return get_data(MODEL, offset, limit)
    

def get_data(MODEL, offset, limit):
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        logger.info(
            f"Executing query for model: {MODEL.__name__} with offset: {offset} and limit: {limit}"
        )
        stmt = select(MODEL).offset(offset).limit(limit)
        results = session.execute(stmt).scalars().all()
        logger.info(f"Query executed successfully, found {len(results)} records")
        # single_dataset = [record.model_dump() for record in results]
    return results
