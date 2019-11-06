import os
import psycopg2
import pytest
from urllib.parse import urljoin

from utils.database import DatabaseHandler
from utils.migrations import HasuraClient, FixturesGenerator


def pytest_addoption(parser):
    parser.addoption(
        "--hasura-endpoint", action="store", default="http://localhost:8080", help="Hasura endpoint"
    )
    parser.addoption(
        "--root", action="store", default="/app", help="Database service root folder"
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption("--hasura-endpoint")


@pytest.fixture
def app_root_folder(request):
    return request.config.getoption("--root")


@pytest.fixture
def postgres_connection():
    return psycopg2.connect(host='postgres', database='postgres', user='postgres')


@pytest.fixture
def enum_table_names():
    return sorted(('vat_types', 'pricing_modes', 'product_states', 'productvariant_states', 'roles'))


@pytest.fixture
def hasura_client(hasura_endpoint):
    return HasuraClient(hasura_endpoint)


@pytest.fixture
def db_handler(postgres_connection):
    return DatabaseHandler(postgres_connection)


@pytest.fixture
def fixtures_project_folder(app_root_folder):
    return os.path.join(app_root_folder, 'fixtures')


@pytest.fixture
def fixtures_generator(app_root_folder, fixtures_project_folder):
    return FixturesGenerator(app_root_folder, fixtures_project_folder)


@pytest.fixture
def small_fixtures(fixtures_generator):
    fixtures_generator.generate('small')
    yield fixtures_generator.project_folder()
    fixtures_generator.cleanup()
