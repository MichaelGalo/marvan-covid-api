from fastapi import FastAPI
from src.dependencies.logger_init import setup_logging
from src.crud.get_single_database import fetch_single_database
from src.config import DATABASE_METADATA

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

    headers_filtered = DATABASE_METADATA.values()
    logger.info(f"{len(headers_filtered)} databases selected")

    try:
        if country != None:
            headers_filtered = [item for item in headers_filtered if country.lower() in item["country"].lower()]

        if keyword != None:
           # Allow for keyword to match where "covid 19" == "covid-19"
           keyword_simple = keyword.lower().replace(" ", "").replace("-", "")
           headers_filtered = [item for item in headers_filtered if keyword_simple in f'{item["country"].lower()}//{item["description"].lower()}//{item["dataset_name"].lower()}'.replace(" ","").replace("-", "")]
        
        logger.info(f"Returning {[item["dataset_name"] for item in headers_filtered]}")

    except Exception as e:
        logger.info(e)
        return {"error": e}
        
    return {"data": headers_filtered}

@app.get("/databases/{database_id}")
async def get_single_database(database_id: int, limit: int = 20, offset: int = 0):
    logger.info(f"Single database endpoint at for database_id={database_id} accessed with query parameters: limit={limit}, offset={offset}")
    data = fetch_single_database(database_id, offset, limit)

    return {"input parameters": {
        "database_id": database_id,
        "limit": limit,
        "offset": offset,
    }, "data": data}

@app.get("/test-endpoint")
async def fetch_test_endpoint():
    try:
        data = fetch_single_database(2, 0, 20)
        logger.info(f"Fetched {len(data)} records from Snowflake.")
        return {"data": data}
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return {"error": str(e)}
