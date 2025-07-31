import re
from datetime import datetime
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
async def get_all_databases(country: str = None, keyword: str = None, last_updated: str = None):
    logger.info(f"Databases endpoint accessed with query parameters: country={country}, keyword={keyword}, last_updated={last_updated}")

    headers_filtered = [dataset for dataset in DATABASE_METADATA.values()]
    logger.info(f"{len(headers_filtered)} databases selected")

    try:
        if country != None:
            headers_filtered = [item for item in headers_filtered if country.lower() in item["country"].lower()]

        if keyword != None:
            # Allow for keyword to match where "covid 19" == "covid-19"
            keyword_simple = keyword.lower().replace(" ", "").replace("-", "")
            headers_filtered = [item for item in headers_filtered if keyword_simple in f'{item["country"].lower()}//{item["description"].lower()}//{item["dataset_name"].lower()}'.replace(" ","").replace("-", "")]

        if last_updated != None:
            date_patterns = [
                ('%Y', r'^\d{4}$'),
                ('%Y-%m', r'^\d{4}-\d{2}$'),
                ('%Y-%m-%d', r'^\d{4}-\d{2}-\d{2}$')
            ]
            input_format = None

            for pattern in date_patterns:
                if re.match(pattern[1], last_updated):
                    input_format = pattern[0]
            if input_format != None:
                headers_filtered = [item for item in headers_filtered if datetime.strptime(item["last_updated"], "%Y-%m-%d") >= datetime.strptime(last_updated, input_format)]
            else:
                logger.info(f"Date input {last_updated} is not in valid format")

                return {"error": "last_updated must be a date in the format YYYY-MM-DD, YYYY-MM, YYYY. Databases will return that have been updated on or since that date."}
        
        logger.info(f"Returning {[item["dataset_name"] for item in headers_filtered]}")
    except Exception as e:
        logger.info(e)
        return {"error": f'{e}'}
    
    for database in headers_filtered:
        try:
            database["data_preview"] = fetch_single_database(database["database_id"], 0, 5)
        except Exception as e:
            logger.error(e)
            raise
        
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
