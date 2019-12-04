from utils import json_helpers
from utils.graphql_client import GraphQLClient
from utils.graphql_helpers import get_query_from_file
from utils.hasura_client import HasuraClient
from utils.stellar_client import StellarClient


import os
import pytest

import urllib.parse


@pytest.fixture(autouse=True)
def graphql_endpoint():
    return 'v1/graphql/'


@pytest.fixture
def graphql_client(hasura_endpoint, graphql_endpoint):
    endpoint = urllib.parse.urljoin(hasura_endpoint, graphql_endpoint)
    client = GraphQLClient(endpoint)
    return client


@pytest.fixture
def hasura_client(hasura_endpoint):
    return HasuraClient(hasura_endpoint)


@pytest.fixture(autouse=True)
def database_seed(database_project_folder, hasura_client, fixtures_project_folder):
    hasura_client.apply_migrations(database_project_folder)
    hasura_client.apply_migrations(fixtures_project_folder)
    yield
    hasura_client.rollback_migrations(fixtures_project_folder)
    hasura_client.rollback_migrations(database_project_folder)


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
def shops_query(graphql_folder, fixtures_set_name):
    call = get_query_from_file(os.path.join(graphql_folder, 'calls'), 'shops')
    response = json_helpers.load(os.path.join(
        graphql_folder, 'responses', fixtures_set_name, 'Consumer', 'Shops.json'))
    return {
        'call': call,
        'response': response
    }


@pytest.fixture
def shop_categories_query(graphql_folder, fixtures_set_name):
    call = get_query_from_file(os.path.join(
        graphql_folder, 'calls'), 'shopCategories')
    response = json_helpers.load(os.path.join(
        graphql_folder, 'responses', fixtures_set_name, 'Consumer', 'Categories.json'))
    return {
        'call': call,
        'response': response
    }
