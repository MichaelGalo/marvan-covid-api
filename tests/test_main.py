import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.main import app
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine

client = TestClient(app)

def test_get_single_database_endpoint_valid():
    with patch('src.main.fetch_single_database') as mock_fetch:
        mock_fetch.return_value = [{'mock': 'data'}]
        response = client.get('/databases/1?limit=5&offset=0')
        assert response.status_code == 200
        data = response.json()
        if 'data' not in data:
            print('Response JSON:', data)
        assert 'data' in data
        assert data['data'] == [{'mock': 'data'}]

def test_get_single_database_endpoint_invalid():
    response = client.get('/databases/99')
    assert response.status_code == 400
    data = response.json()
    assert 'detail' in data
    assert 'invalid' in data['detail'].lower()

def test_get_all_databases_endpoint():
    response = client.get('/databases/?country=US&keyword=test&last_updated=123')
    assert response.status_code == 200
    data = response.json()
    assert 'input parameters' in data
    assert data['input parameters']['country'] == 'US'
    assert data['input parameters']['keyword'] == 'test'
    assert data['input parameters']['last_updated'] == 123


def test_snowflake_connection_ping():
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            value = result.scalar()
            assert value == 1
    except Exception as e:
        pytest.fail(f"Could not connect to Snowflake or execute query: {e}")

def test_snowflake_current_database():
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT CURRENT_DATABASE()")
            db = result.scalar()
            assert db is not None
            assert isinstance(db, str)
            assert db != ""
    except Exception as e:
        pytest.fail(f"Could not fetch current database: {e}")

def test_snowflake_current_schema():
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            result = conn.execute("SELECT CURRENT_SCHEMA()")
            schema = result.scalar()
            assert schema is not None
            assert isinstance(schema, str)
            assert schema != ""
    except Exception as e:
        pytest.fail(f"Could not fetch current schema: {e}")

def test_snowflake_list_tables():
    engine = sqlalchemy_engine()
    try:
        with engine.connect() as conn:
            result = conn.execute("SHOW TABLES")
            tables = result.fetchall()
            assert tables is not None
            # It's possible there are no tables, so just check for no exception
    except Exception as e:
        pytest.fail(f"Could not list tables: {e}")