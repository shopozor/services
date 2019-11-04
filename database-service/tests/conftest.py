import pytest
from urllib.parse import urljoin


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
