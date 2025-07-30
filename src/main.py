from fastapi import FastAPI
from src.dependencies.logger_init import setup_logging
from src.crud.us_deathcounts import fetch_us_deathcounts

app = FastAPI()

logger = setup_logging()

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to the FastAPI demo! Visit /docs for API documentation and how to use this."
    }

@app.get("/us-deathcounts")
async def fetch_us_deathcounts_endpoint():
    try:
        data = fetch_us_deathcounts()
        logger.info(f"Fetched {len(data)} records from CLN_US_DEATHCOUNTS.")
        return {"data": data}
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return {"error": str(e)}