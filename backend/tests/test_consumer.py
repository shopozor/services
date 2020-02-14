from utils.api_test import assert_graphql_query_works


def test_consumer_should_get_shops_list(graphql_client, shops_query):
    assert_graphql_query_works(graphql_client, shops_query)


def test_consumer_should_get_shop_categories(graphql_client, shop_categories_query):
    assert_graphql_query_works(graphql_client, shop_categories_query)


def test_consumer_should_get_shop_details(graphql_client, shop_queries):
    for query in shop_queries:
        assert_graphql_query_works(graphql_client, query)