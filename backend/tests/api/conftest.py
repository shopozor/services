from utils import json_helpers
from utils.graphql_helpers import get_query_from_file

import os
import pytest


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
