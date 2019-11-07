def test_shopozor_structural_migrations_can_be_rolled_back(hasura_client, app_root_folder, db_handler):
    # Given I've applied structural migrations
    project_folder = app_root_folder
    result = hasura_client.apply_migrations(project_folder)
    assert 0 == result.exit_code

    # When I revert the migrations
    result = hasura_client.rollback_migrations(project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    assert db_handler.is_database_empty()


def test_fixtures_migrations_can_be_rolled_back(hasura_client, app_root_folder, small_fixtures, db_handler, enum_table_names):
    # Given I've applied fixtures migrations
    structural_project_folder = app_root_folder
    hasura_client.apply_migrations(structural_project_folder)
    hasura_client.apply_migrations(small_fixtures)

    # When I revert the fixtures data
    result = hasura_client.rollback_migrations(small_fixtures)

    # Then I get no errors
    assert 0 == result.exit_code
    # And only the enum tables are not empty
    assert enum_table_names == db_handler.get_non_empty_tables()

    # When I revert the structural migrations
    result = hasura_client.rollback_migrations(structural_project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    assert db_handler.is_database_empty()
