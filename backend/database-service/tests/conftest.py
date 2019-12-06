from utils.hasura_client import HasuraClient

import os
import psycopg2
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--database-service-folder', action='store', default='/app/database-service', help='Database service folder'
    )
    parser.addoption(
        '--fixtures-folder', action='store', default='/app/fixtures', help='Fixtures folder'
    )
    parser.addoption(
        '--hasura-endpoint', action='store', default='http://localhost:8080', help='Hasura endpoint'
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption('--hasura-endpoint')


@pytest.fixture
def database_project_folder(request):
    return request.config.getoption('--database-service-folder')


@pytest.fixture
def fixtures_folder(request):
    return request.config.getoption('--fixtures-folder')


@pytest.fixture
def fixtures_project_folder(fixtures_folder):
    return os.path.join(
        fixtures_folder, 'database')


@pytest.fixture
def fixtures_set(hasura_client, fixtures_project_folder):
    yield fixtures_project_folder
    hasura_client.rollback_migrations(fixtures_project_folder)


@pytest.fixture
def hasura_client(hasura_endpoint, database_project_folder):
    client = HasuraClient(hasura_endpoint)
    yield client
    client.rollback_migrations(database_project_folder)


@pytest.fixture
def postgres_connection():
    conn = psycopg2.connect(
        host='postgres', database='postgres', user='postgres', password='')
    yield conn
    conn.close()


@pytest.fixture
def expected_pricing_modes():
    return ['AUTO_PRICE', 'AUTO_UNIT', 'BULK', 'FREE']


@pytest.fixture
def expected_product_states():
    return ['VISIBLE', 'INVISIBLE', 'DELETED']


@pytest.fixture
def expected_productvariant_states():
    return ['VISIBLE', 'INVISIBLE', 'DELETED', 'CHANGE_ASAP']


@pytest.fixture
def expected_roles():
    return ['REX', 'MANAGER', 'SOFTOZOR']


@pytest.fixture
def expected_vat_types():
    return ['SERVICES', 'PRODUCTS', 'SPECIAL']
