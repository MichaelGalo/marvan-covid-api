import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.main import app
from src.crud.get_single_database import fetch_single_database

client = TestClient(app)

# --- Tests for fetch_single_database ---

def test_fetch_single_database_valid_ids():
    # Patch the SQLAlchemy session and model_dump
    with patch('src.crud.get_single_database.Session') as mock_session, \
         patch('src.crud.get_single_database.sqlalchemy_engine') as mock_engine:
        mock_engine.return_value = MagicMock()
        mock_session.return_value.__enter__.return_value = MagicMock()
        # Mock the model_dump method
        mock_record = MagicMock()
        mock_record.model_dump.return_value = {'mock': 'data'}
        mock_results = [mock_record] * 3
        mock_session.return_value.__enter__.return_value.execute.return_value.scalars.return_value.all.return_value = mock_results
        for db_id in [1, 2, 3, 4]:
            result = fetch_single_database(db_id, 0, 10)
            assert isinstance(result, list)
            assert result == [{'mock': 'data'}] * 3

def test_fetch_single_database_invalid_id():
    with pytest.raises(ValueError):
        fetch_single_database(99, 0, 10)
    with pytest.raises(ValueError):
        fetch_single_database(None, 0, 10)

# --- Tests for FastAPI endpoints ---

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
    with patch('src.main.fetch_single_database', side_effect=ValueError('Invalid database_id provided.')):
        response = client.get('/databases/99')
        assert response.status_code == 400
        data = response.json()
        assert 'detail' in data
        assert data['detail'] == 'Invalid database_id provided.'

def test_get_all_databases_endpoint():
    response = client.get('/databases/?country=US&keyword=test&last_updated=123')
    assert response.status_code == 200
    data = response.json()
    assert 'input parameters' in data
    assert data['input parameters']['country'] == 'US'
    assert data['input parameters']['keyword'] == 'test'
    assert data['input parameters']['last_updated'] == 123

def test_test_endpoint_success():
    with patch('src.main.fetch_single_database') as mock_fetch:
        mock_fetch.return_value = [{'mock': 'data'}]
        response = client.get('/test-endpoint')
        assert response.status_code == 200
        data = response.json()
        if 'data' not in data:
            print('Response JSON:', data)
        assert 'data' in data
        assert data['data'] == [{'mock': 'data'}]

def test_test_endpoint_error():
    with patch('src.main.fetch_single_database', side_effect=Exception('fail')):
        response = client.get('/test-endpoint')
        assert response.status_code == 200
        data = response.json()
        if 'error' not in data:
            print('Response JSON:', data)
        assert 'error' in data
        assert data['error'] == 'fail'