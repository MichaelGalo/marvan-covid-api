from fastapi import FastAPI
from src.dependencies.logger_init import setup_logging
from src.crud.us_deathcounts import fetch_us_deathcounts
from src.crud.uk_cases_by_day import fetch_uk_cases_by_day

app = FastAPI()

logger = setup_logging()

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to the FastAPI demo! Visit /docs for API documentation and how to use this."
    }


@app.get("/test-endpoint")
async def fetch_test_endpoint():
    try:
        data = fetch_uk_cases_by_day()
        logger.info(f"Fetched {len(data)} records from Snowflake.")
        return {"data": data}
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return {"error": str(e)}