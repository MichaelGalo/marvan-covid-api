from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from src.dependencies.logger_init import setup_logging
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine
from src.main import app

logger = setup_logging()

client = TestClient(app)


def test_get_single_database_endpoint_valid():
    with patch("src.main.fetch_single_database") as mock_fetch:
        mock_fetch.return_value = [{"mock": "data"}]
        logger.info("Testing valid single database endpoint request")
        response = client.get("/databases/1?limit=5&offset=0")
        logger.info(f"Response status: {response.status_code}")
        assert response.status_code == 200
        data = response.json()
        logger.info(f"Response JSON: {data}")
        if "data" not in data:
            print("Response JSON:", data)
        assert "data" in data
        assert data["data"] == [{"mock": "data"}]


def test_get_single_database_endpoint_invalid():
    logger.info("Testing invalid single database endpoint request")
    response = client.get("/databases/99")
    logger.info(f"Response status: {response.status_code}")
    assert response.status_code == 400
    data = response.json()
    logger.info(f"Response JSON: {data}")
    assert "detail" in data
    assert "invalid" in data["detail"].lower()


def test_snowflake_connection_ping():
    logger.info("Testing Snowflake connection ping")
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            logger.info("Connected to Snowflake")
            result = conn.execute(text("SELECT 1"))
            value = result.scalar()
            logger.info(f"SELECT 1 result: {value}")
            assert value == 1
    except Exception as e:
        logger.info(f"Exception during Snowflake ping: {e}")
        pytest.fail(f"Could not connect to Snowflake or execute query: {e}")


def test_snowflake_current_database():
    logger.info("Testing Snowflake current database query")
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            logger.info("Connected to Snowflake")
            result = conn.execute(text("SELECT CURRENT_DATABASE()"))
            db = result.scalar()
            logger.info(f"CURRENT_DATABASE() result: {db}")
            assert db is not None
            assert isinstance(db, str)
            assert db != ""
    except Exception as e:
        logger.info(f"Exception during CURRENT_DATABASE(): {e}")
        pytest.fail(f"Could not fetch current database: {e}")


def test_snowflake_current_schema():
    logger.info("Testing Snowflake current schema query")
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            logger.info("Connected to Snowflake")
            result = conn.execute(text("SELECT CURRENT_SCHEMA()"))
            schema = result.scalar()
            logger.info(f"CURRENT_SCHEMA() result: {schema}")
            assert schema is not None
            assert isinstance(schema, str)
            assert schema != ""
    except Exception as e:
        logger.info(f"Exception during CURRENT_SCHEMA(): {e}")
        pytest.fail(f"Could not fetch current schema: {e}")


def test_snowflake_list_tables():
    logger.info("Testing Snowflake list tables query")
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            logger.info("Connected to Snowflake")
            result = conn.execute(text("SHOW TABLES"))
            tables = result.fetchall()
            logger.info(f"SHOW TABLES result: {tables}")
            assert tables is not None
            # It's possible there are no tables, so just check for no exception
    except Exception as e:
        logger.info(f"Exception during SHOW TABLES: {e}")
        pytest.fail(f"Could not list tables: {e}")
