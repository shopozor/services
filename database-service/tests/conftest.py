import pytest
from urllib.parse import urljoin


def pytest_addoption(parser):
    parser.addoption(
        "--hasura-endpoint", action="store", default="http://localhost:8080", help="Hasura endpoint"
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption("--hasura-endpoint")
