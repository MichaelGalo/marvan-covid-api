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

