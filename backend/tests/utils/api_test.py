def assert_graphql_query_works(graphql_client, query):
    response = graphql_client.execute(query['call'])
    expected_response = query['response']
    assert expected_response == response