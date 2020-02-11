from common_utils import json_helpers
from common_utils.graphql_client import GraphQLClient
from common_utils.graphql_helpers import get_query_from_file
from common_utils.stellar_client import StellarClient

import os
import pytest
import urllib.parse


def pytest_addoption(parser):
    parser.addoption(
        "--fixtures-folder", action="store", default="/app/fixtures", help="Fixtures folder"
    )
    parser.addoption(
        "--graphql-folder", action="store", default="/app/fixtures/graphql", help="Folder containing the graphql calls and responses"
    )
    parser.addoption(
        "--hasura-endpoint", action="store", default="http://localhost:8080", help="Hasura endpoint"
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption('--hasura-endpoint')


@pytest.fixture
def graphql_folder(request):
    return request.config.getoption('--graphql-folder')


@pytest.fixture(autouse=True)
def graphql_endpoint():
    return 'v1/graphql/'


@pytest.fixture
def graphql_client(hasura_endpoint, graphql_endpoint):
    endpoint = urllib.parse.urljoin(hasura_endpoint, graphql_endpoint)
    client = GraphQLClient(endpoint)
    return client


@pytest.fixture(autouse=True)
def stellar_snapshot():
    client = StellarClient('shopozor-api-tests')
    client.create_snapshot()
    has_worked = client.list_snapshots()
    assert has_worked is True
    yield
    client.restore_snapshot()
    client.remove_snapshot()


@pytest.fixture
def shops_query(graphql_folder):
    call = get_query_from_file(os.path.join(graphql_folder, 'calls'), 'shops')
    response = json_helpers.load(os.path.join(
        graphql_folder, 'responses', 'Consumer', 'Shops.json'))
    return {
        'call': call,
        'response': response
    }


@pytest.fixture
def shop_categories_query(graphql_folder):
    call = get_query_from_file(os.path.join(
        graphql_folder, 'calls'), 'shopCategories')
    response = json_helpers.load(os.path.join(
        graphql_folder, 'responses', 'Consumer', 'Categories.json'))
    return {
        'call': call,
        'response': response
    }


@pytest.fixture
def shop_queries(graphql_folder):
    call = get_query_from_file(os.path.join(graphql_folder, 'calls'), 'shop')
    # TODO: put the number of shops (5) in the config somehow!
    return [{
        'call': call,
        'variables': {'shopId': id},
        'response': json_helpers.load(os.path.join(graphql_folder, 'responses', 'Consumer', 'Shops', f'Shop-{id}.json'))
    } for id in range(1, 5)]
