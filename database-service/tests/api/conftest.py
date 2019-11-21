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
def database_seed(app_root_folder, hasura_client, fixtures_project_folder):
    hasura_client.apply_migrations(app_root_folder)
    hasura_client.apply_migrations(fixtures_project_folder)
    yield
    hasura_client.rollback_migrations(fixtures_project_folder)
    hasura_client.rollback_migrations(app_root_folder)


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
def shops_query(graphql_calls_folder):
    return get_query_from_file(graphql_calls_folder, 'shops')