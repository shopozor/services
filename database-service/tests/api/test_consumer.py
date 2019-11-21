def test_consumer_should_get_shops_list(graphql_client, shops_query):
    response = graphql_client.execute(shops_query['call'])
    expected_response = shops_query['response']
    assert expected_response == response