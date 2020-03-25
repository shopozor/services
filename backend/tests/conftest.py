from test_utils import json_helpers
from test_utils.graphql_client import GraphQLClient
from test_utils.graphql_helpers import get_query_from_file
from test_utils.stellar_client import StellarClient

import os
import pytest
import urllib.parse


def pytest_addoption(parser):
    parser.addoption(
        "--fixtures-folder", action="store", default="/app/fixtures", help="Fixtures folder"
    )
    parser.addoption(
        "--graphql-responses-folder", action="store", default="/app/shared/fixtures/graphql", help="Folder containing the graphql responses"
    )
    parser.addoption(
        "--graphql-calls-folder", action="store", default="/app/shared/graphql", help="Folder containing the graphql calls"
    )
    parser.addoption(
        "--hasura-endpoint", action="store", default="http://localhost:8080", help="Hasura endpoint"
    )


@pytest.fixture
def hasura_endpoint(request):
    return request.config.getoption('--hasura-endpoint')


@pytest.fixture
def graphql_responses_folder(request):
    return request.config.getoption('--graphql-responses-folder')


@pytest.fixture
def graphql_calls_folder(request):
    return request.config.getoption('--graphql-calls-folder')


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
def shops_query(graphql_calls_folder, graphql_responses_folder):
    call = get_query_from_file(graphql_calls_folder, 'shops')
    response = json_helpers.load(os.path.join(
        graphql_responses_folder, 'responses', 'Consumer', 'Shops.json'))
    return {
        'call': call,
        'response': response
    }


@pytest.fixture
def shop_categories_query(graphql_calls_folder, graphql_responses_folder):
    call = get_query_from_file(graphql_calls_folder, 'shopCategories')
    response = json_helpers.load(os.path.join(
        graphql_responses_folder, 'responses', 'Consumer', 'Categories.json'))
    return {
        'call': call,
        'response': response
    }


@pytest.fixture
def shop_queries(graphql_calls_folder, graphql_responses_folder):
    call = get_query_from_file(graphql_calls_folder, 'shop')
    # TODO: put the number of shops (5) in the config somehow!
    return [{
        'call': call,
        'variables': {'shopId': id},
        'response': json_helpers.load(os.path.join(graphql_responses_folder, 'responses', 'Consumer', 'Shops', f'Shop-{id}.json'))
    } for id in range(1, 5)]
