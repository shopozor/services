import os
import sh
import shutil


def apply_migrations(hasura_endpoint, migrations_folder):
    cmd = sh.Command('hasura')
    return cmd('migrate', 'apply', '--endpoint', hasura_endpoint, '--project', migrations_folder, '--skip-update-check')


def test_shopozor_structural_migrations_can_be_applied(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    project_folder = app_root_folder

    # When I apply the migrations
    result = apply_migrations(hasura_endpoint, project_folder)

    # Then I get no errors
    assert 0 == result.exit_code


def get_number_of_migrations_in_folder(folder):
    return os.listdir(folder) / 2


def rollback_migrations(hasura_endpoint, migrations_folder):
    cmd = sh.Command('hasura')
    nb_migrations = get_number_of_migrations_in_folder(migrations_folder)
    return cmd('migrate', 'apply', '--down', nb_migrations, '--endpoint', hasura_endpoint, '--project', migrations_folder, '--skip-update-check')


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
    result = apply_migrations(hasura_endpoint, project_folder)
    assert 0 == result.exit_code

    # When I revert the migrations
    result = rollback_migrations(hasura_endpoint, project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    assert is_database_empty(postgres_connection)


def cleanup_fixtures(fixtures_dir):
    if os.path.isdir(fixtures_dir):
        shutil.rmtree(fixtures_dir)


def generate_fixtures(app_root_folder, fixtures_set, fixtures_output_dir):
    cleanup_fixtures(fixtures_output_dir)
    cmd = sh.Command(os.path.join(app_root_folder, 'tests',
                                  'fixtures-generator', 'entrypoint.sh'))
    migrations_output_dir = os.path.join(fixtures_output_dir, 'migrations')
    return cmd(fixtures_set, fixtures_output_dir, migrations_output_dir, app_root_folder)


def test_fixtures_migrations_can_be_applied(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    structural_project_folder = app_root_folder
    # Given I've generated the fixtures
    fixtures_project_folder = os.path.join(app_root_folder, 'fixtures')
    generate_fixtures(app_root_folder, 'small', fixtures_project_folder)

    # When I apply the migrations
    structural_migration_result = apply_migrations(
        hasura_endpoint, app_root_folder)
    fixtures_migration_result = apply_migrations(
        hasura_endpoint, fixtures_project_folder)

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
    generate_fixtures(app_root_folder, 'small', fixtures_project_folder)
    apply_migrations(hasura_endpoint, app_root_folder)
    apply_migrations(hasura_endpoint, fixtures_project_folder)

    # When I revert the fixtures data
    result = rollback_migrations(hasura_endpoint, fixtures_project_folder)

    # Then I get no errors
    assert 0 == result.exit_code
    # And the database is empty
    assert enum_table_names == get_non_empty_tables(postgres_connection)
