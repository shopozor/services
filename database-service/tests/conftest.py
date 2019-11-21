import os
import pytest

from utils.migrations import HasuraClient


def pytest_addoption(parser):
    parser.addoption(
        "--hasura-endpoint", action="store", default="http://localhost:8080", help="Hasura endpoint"
    )
    parser.addoption(
        "--root", action="store", default="/app", help="Database service root folder"
    )
    parser.addoption(
        "--fixtures-set", action="store", default="small", help="Fixtures set (tiny, small, medium, large)"
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption("--hasura-endpoint")


@pytest.fixture
def app_root_folder(request):
    return request.config.getoption("--root")


@pytest.fixture
def fixtures_set(request, app_root_folder, hasura_client):
    option = request.config.getoption("--fixtures-set")
    fixtures_project_folder = os.path.join(
        app_root_folder, 'fixtures', 'database', option)
    yield fixtures_project_folder
    hasura_client.rollback_migrations(fixtures_project_folder)


@pytest.fixture
def hasura_client(hasura_endpoint, app_root_folder):
    client = HasuraClient(hasura_endpoint)
    yield client
    client.rollback_migrations(app_root_folder)