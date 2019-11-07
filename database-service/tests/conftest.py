import os
import pytest

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
def hasura_client(hasura_endpoint, app_root_folder):
    client = HasuraClient(hasura_endpoint)
    yield client
    client.rollback_migrations(app_root_folder)


@pytest.fixture
def fixtures_project_folder(app_root_folder):
    return os.path.join(app_root_folder, 'fixtures')


@pytest.fixture
def fixtures_generator(app_root_folder, fixtures_project_folder):
    return FixturesGenerator(app_root_folder, fixtures_project_folder)


@pytest.fixture
def small_fixtures(fixtures_generator, hasura_client):
    fixtures_generator.generate('small')
    yield fixtures_generator.project_folder()
    hasura_client.rollback_migrations(fixtures_generator.project_folder())
    fixtures_generator.cleanup()
