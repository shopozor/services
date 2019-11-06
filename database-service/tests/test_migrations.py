import os

from utils.database import DatabaseHandler
from utils.migrations import HasuraClient, FixturesGenerator


def test_shopozor_structural_migrations_can_be_applied(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    project_folder = app_root_folder

    # When I apply the migrations
    hasura_client = HasuraClient(hasura_endpoint)
    result = hasura_client.apply_migrations(project_folder)

    # Then I get no errors
    assert 0 == result.exit_code


def test_shopozor_structural_migrations_can_be_rolled_back(hasura_endpoint, app_root_folder, postgres_connection):
    # Given I've applied structural migrations
    project_folder = app_root_folder
    hasura_client = HasuraClient(hasura_endpoint)
    result = hasura_client.apply_migrations(project_folder)
    assert 0 == result.exit_code

    # When I revert the migrations
    result = hasura_client.rollback_migrations(project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    db_handler = DatabaseHandler(postgres_connection)
    assert db_handler.is_database_empty()


def test_fixtures_migrations_can_be_applied(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    structural_project_folder = app_root_folder
    # Given I've generated the fixtures
    fixtures_project_folder = os.path.join(app_root_folder, 'fixtures')
    generator = FixturesGenerator(app_root_folder, fixtures_project_folder)
    generator.generate('small')

    # When I apply the migrations
    hasura_client = HasuraClient(hasura_endpoint)
    structural_migration_result = hasura_client.apply_migrations(
        app_root_folder)
    fixtures_migration_result = hasura_client.apply_migrations(
        fixtures_project_folder)

    # Then I get no errors
    assert 0 == structural_migration_result.exit_code
    assert 0 == fixtures_migration_result.exit_code


def test_fixtures_migrations_can_be_rolled_back(hasura_endpoint, app_root_folder, postgres_connection, enum_table_names):
    # Given I've applied fixtures migrations
    structural_project_folder = app_root_folder
    fixtures_project_folder = os.path.join(app_root_folder, 'fixtures')
    generator = FixturesGenerator(app_root_folder, fixtures_project_folder)
    generator.generate('small')
    hasura_client = HasuraClient(hasura_endpoint)
    hasura_client.apply_migrations(app_root_folder)
    hasura_client.apply_migrations(fixtures_project_folder)

    # When I revert the fixtures data
    result = hasura_client.rollback_migrations(fixtures_project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    db_handler = DatabaseHandler(postgres_connection)
    assert enum_table_names == db_handler.get_non_empty_tables(
        postgres_connection)
