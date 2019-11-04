import os
import sh
import shutil


def apply_migrations(hasura_endpoint, migrations_folder):
    cmd = sh.Command('hasura')
    return cmd('migrate', 'apply', '--endpoint', hasura_endpoint, '--project', migrations_folder, '--skip-update-check')


def test_shopozor_structural_migrations_can_be_applied_without_errors(hasura_endpoint, app_root_folder):
    # Given I've structural project migrations
    project_folder = app_root_folder

    # When I apply the migrations
    result = apply_migrations(hasura_endpoint, project_folder)

    # Then I get no errors
    assert 0 == result.exit_code


def cleanup_fixtures(fixtures_dir):
    if os.path.isdir(fixtures_dir):
        shutil.rmtree(fixtures_dir)


def generate_fixtures(app_root_folder, fixtures_set, fixtures_output_dir):
    cleanup_fixtures(fixtures_output_dir)
    cmd = sh.Command(os.path.join(app_root_folder, 'tests',
                                  'fixtures-generator', 'entrypoint.sh'))
    migrations_output_dir = os.path.join(fixtures_output_dir, 'migrations')
    return cmd(fixtures_set, fixtures_output_dir, migrations_output_dir, app_root_folder)


def test_fixtures_migrations_can_be_applied_without_errors(hasura_endpoint, app_root_folder):
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
