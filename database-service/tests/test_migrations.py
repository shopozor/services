import os
import sh
import shutil

from utils.migrations import HasuraClient, FixturesGenerator


def test_shopozor_structural_migrations_can_be_applied(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    project_folder = app_root_folder

    # When I apply the migrations
    hasura_client = HasuraClient(hasura_endpoint)
    result = hasura_client.apply_migrations(project_folder)

    # Then I get no errors
    assert 0 == result.exit_code


def get_tables_list_from_database(conn):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    return cursor.fetchall()


def is_database_empty(conn):
    tables_list = get_tables_list_from_database(conn)
    return 0 == len(tables_list)


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
    assert is_database_empty(postgres_connection)


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


def get_non_empty_tables(postgres_connection):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT relname FROM pg_stat_all_tables WHERE schemaname = 'public' AND n_tup_ins > 0")
    table_names = cursor.fetchall()
    return sorted(tuple(item[0] for item in table_names))


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
    assert enum_table_names == get_non_empty_tables(postgres_connection)
