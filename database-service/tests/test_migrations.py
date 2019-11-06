def test_shopozor_structural_migrations_can_be_applied(hasura_client, app_root_folder):
    # Given I've structural project migrations
    project_folder = app_root_folder

    # When I apply the migrations
    result = hasura_client.apply_migrations(project_folder)

    # Then I get no errors
    assert 0 == result.exit_code


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


def test_fixtures_migrations_can_be_applied(hasura_client, app_root_folder, fixtures_generator):
    # Given I've structural project migrations
    structural_project_folder = app_root_folder
    # Given I've generated the fixtures
    fixtures_generator.generate('small')

    # When I apply the migrations
    structural_migration_result = hasura_client.apply_migrations(
        app_root_folder)
    fixtures_migration_result = hasura_client.apply_migrations(
        fixtures_generator.project_folder())

    # Then I get no errors
    assert 0 == structural_migration_result.exit_code
    assert 0 == fixtures_migration_result.exit_code


def test_fixtures_migrations_can_be_rolled_back(hasura_client, app_root_folder, fixtures_generator, db_handler, enum_table_names):
    # Given I've applied fixtures migrations
    structural_project_folder = app_root_folder
    fixtures_generator.generate('small')
    hasura_client.apply_migrations(app_root_folder)
    hasura_client.apply_migrations(fixtures_generator.project_folder())

    # When I revert the fixtures data
    result = hasura_client.rollback_migrations(
        fixtures_generator.project_folder())

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    assert enum_table_names == db_handler.get_non_empty_tables()
