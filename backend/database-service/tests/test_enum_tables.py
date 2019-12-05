def test_pricing_modes_enum(database_project_folder, expected_pricing_modes, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    project_folder = database_project_folder
    has_worked = hasura_client.apply_migrations(project_folder)
    assert has_worked is True

    # When I ask for the pricing_modes
    cursor = postgres_connection.cursor()
    cursor.execute('SELECT mode FROM pricing_modes')
    actual = [item[0] for item in cursor.fetchall()].sort()
    cursor.close()

    # Then
    assert expected_pricing_modes == actual