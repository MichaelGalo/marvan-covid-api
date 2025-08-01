# Marvan COVID API

This project provides a FastAPI-based REST API for users to securely access COVID-related data from our Snowflake data warehouse.

## Overview

- **FastAPI** is used to build a high-performance, easy-to-use API for data access.
- **Snowflake** serves as the backend data warehouse, storing and managing all COVID data.
- The API enables users to query, filter, and retrieve data programmatically for analytics, reporting, and integration purposes.

## Features

- Secure, authenticated endpoints for data access
- FastAPI auto-generates interactive API documentation (Swagger UI)
- Efficient querying and data retrieval from Snowflake
- Modular codebase for easy extension and maintenance

## API Endpoints

The following endpoints are available:

- `GET /` — Root endpoint, welcome message and redirect to the swagger docs.
- `GET /data/datasets` — List all datasets (optional filters: `country`, `keyword`, `last_updated`).
- `GET /data/datasets/{dataset_id}` — Get a single dataset by ID (optional: `limit`, `offset`).
- `GET /data/countries` — List all countries and their datasets (optional: `limit`, `offset`).
- `GET /data/countries/{country_name}` — Get all datasets for a specific country (optional: `limit`, `offset`).


## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Snowflake credentials** in your environment or a config file.
3. **Run the API server:**
   ```bash
   uvicorn src.main:app --reload
   ```
4. **Access the API docs:**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive documentation.

