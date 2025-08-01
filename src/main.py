import re
from datetime import datetime

from fastapi import FastAPI, HTTPException

from src.crud.get_single_dataset import fetch_single_dataset
from src.dependencies.logger_init import setup_logging

app = FastAPI()

logger = setup_logging()


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to the data portal! Visit /docs for API documentation and usage instructions."
    }

@app.get("/data/datasets", tags=["Datasets"])
async def get_all_datasets(
    country: str = None, keyword: str = None, last_updated: str = None
):
    logger.info(
        f"Datasets endpoint accessed with query parameters: country={country}, keyword={keyword}, last_updated={last_updated}"
    )
    response = fetch_single_dataset(0, 0, 1000)

    headers_filtered = [
        {
            "dataset_id": header.DATASET_ID,
            "country": header.COUNTRY,
            "dataset_name": header.DATASET_NAME,
            "description": header.DESCRIPTION,
            "last_updated": header.LAST_UPDATED
        }
        for header in response
    ]
        
    logger.info(f"{len(headers_filtered)} datasets found")

    try:
        if country != None:
            headers_filtered = [
                item
                for item in headers_filtered
                if country.lower().replace(" ", "")
                in f'{item["country"].lower()}'.replace(
                    " ", ""
                )
            ]

        if keyword != None:
            # Allow for keyword to match where "covid 19" == "covid-19"
            keyword_simple = keyword.lower().replace(" ", "").replace("-", "")
            headers_filtered = [
                item
                for item in headers_filtered
                if keyword_simple
                in f'{item["country"].lower()}//{item["description"].lower()}//{item["dataset_name"].lower()}'.replace(
                    " ", ""
                ).replace(
                    "-", ""
                )
            ]

        if last_updated != None:
            date_patterns = [
                ("%Y", r"^\d{4}$"),
                ("%Y-%m", r"^\d{4}-\d{2}$"),
                ("%Y-%m-%d", r"^\d{4}-\d{2}-\d{2}$"),
            ]
            input_format = None

            for pattern in date_patterns:
                if re.match(pattern[1], last_updated):
                    input_format = pattern[0]
            if input_format != None:
                headers_filtered = [
                    item
                    for item in headers_filtered
                    if datetime.strptime(item["last_updated"], "%Y-%m-%d")
                    >= datetime.strptime(last_updated, input_format)
                ]
            else:
                logger.info(f"Date input {last_updated} is not in valid format")

                return HTTPException(status_code=400, detail="last_updated must be a date in the format YYYY-MM-DD, YYYY-MM, YYYY. Datasets will returned that have been updated on or since that date.")

        logger.info(f"Returning {[item['dataset_name'] for item in headers_filtered]}")
    except Exception as e:
        logger.info(e)
        return HTTPException(status_code=400, detail=str(e))

    for dataset in headers_filtered:
        try:
            dataset["data_preview"] = fetch_single_dataset(
                dataset["dataset_id"], 0, 1
            )
        except Exception as e:
            logger.error(e)
            return HTTPException(status_code=500, detail=str(e))

    return {"data": headers_filtered}

@app.get("/data/datasets/{dataset_id}", tags=["Datasets"])
async def get_single_dataset(dataset_id: int, limit: int = 20, offset: int = 0):
    logger.info(
        f"Single dataset endpoint for dataset_id={dataset_id} accessed with query parameters: limit={limit}, offset={offset}"
    )
    try:
        data = fetch_single_dataset(dataset_id, offset, limit)

        headers = fetch_single_dataset(0, 0, 1000)
        data_header = None
        for header in headers:
            if header.DATASET_ID == dataset_id:
                data_header = header
                logger.info(f"Header successfully located for dataset_id={dataset_id}")
                break

    except ValueError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "dataset_id": data_header.DATASET_ID,
        "country": data_header.COUNTRY,
        "dataset_name": data_header.DATASET_NAME,
        "description": data_header.DESCRIPTION,
        "last_updated": data_header.LAST_UPDATED,
        "limit": limit,
        "offset": offset,
        "data": data,
    }

@app.get("/data/countries", tags=["Countries"])
async def get_countries(offset: int = 0, limit: int = 20):
    logger.info(f"/data/countries endpoint accessed with query parameters: offset={offset}, limit={limit}.")
    try:
        response = fetch_single_dataset(0, offset, limit)
        countries = set([dataset.COUNTRY for dataset in response])
        data = {country: {"datasets": []} for country in countries}
        for dataset in response:
            data[f"{dataset.COUNTRY}"]["datasets"].append({
                "dataset_name": dataset.DATASET_NAME,
                "dataset_id": dataset.DATASET_ID
            })
    except ValueError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "offset": offset,
        "limit": limit,
        "data": data
    }

@app.get("/data/countries/{country_name}", tags=["Countries"])
async def get_country_data(country_name: str, offset: int = 0, limit: int = 20):
    logger.info(f"/data/countres/country_name endpoint accessed with parameters: country_name={country_name}, offset={offset}, limit={limit}")
    try:
        response = fetch_single_dataset(0, offset, limit)
        country_datasets = [
            dataset
            for dataset in response
            if country_name.lower() in dataset.COUNTRY.lower()
        ]

        data = []
        for dataset in country_datasets:
            try:
                preview = fetch_single_dataset(dataset.DATASET_ID, 0, 1)
                data.append({
                    "dataset_id": dataset.DATASET_ID,
                    "country": dataset.COUNTRY,
                    "dataset_name": dataset.DATASET_NAME,
                    "description": dataset.DESCRIPTION,
                    "last_updated": dataset.LAST_UPDATED,
                    "data_preview": preview
                })
            except Exception as e:
                logger.error(e)
                return HTTPException(status_code=500, detail=str(e))

    except ValueError as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "country_name": country_name,
        "offset": offset,
        "limit": limit,
        "data": data
    }
