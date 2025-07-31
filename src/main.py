from fastapi import FastAPI
from src.dependencies.logger_init import setup_logging
from src.crud.ca_rapidtestdemand import fetch_ca_rapidtestdemand

app = FastAPI()

logger = setup_logging()

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to the FastAPI demo! Visit /docs for API documentation and how to use this."
    }

@app.get("/databases/")
async def get_all_databases(country: str = None, keyword: str = None, last_updated: int = None):
    logger.info(f"Databases endpoint accessed with query parameters: country={country}, keyword={keyword}, last_updated={last_updated}")

    return {"input parameters": {
        "country": country,
        "keyword": keyword,
        "last_updated": last_updated
    }}

@app.get("/databases/{database_id}")
async def get_single_database(database_id: int, limit: int = 20, offset: int = 0):
    logger.info(f"Single database endpoint at for database_id={database_id} accessed with query parameters: limit={limit}, offset={offset}")

    return {"input parameters": {
        "database_id": database_id,
        "limit": limit,
        "offset": offset
    }}

@app.get("/test-endpoint")
async def fetch_test_endpoint():
    try:
        data = fetch_ca_rapidtestdemand() 
        logger.info(f"Fetched {len(data)} records from Snowflake.")
        return {"data": data}
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return {"error": str(e)}
