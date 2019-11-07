def test_shopozor_structural_migrations_can_be_applied(hasura_client, app_root_folder):
    # Given I have structural migrations
    project_folder = app_root_folder

    # When I apply them
    exit_code = hasura_client.apply_migrations(project_folder)

    # Then I get no error
    assert 0 == exit_code


def test_fixtures_migrations_can_be_applied(hasura_client, app_root_folder, small_fixtures):
    # Given I've applied structural migrations
    structural_project_folder = app_root_folder
    exit_code = hasura_client.apply_migrations(structural_project_folder)
    assert 0 == exit_code

    # When I apply the fixtures migrations
    exit_code = hasura_client.apply_migrations(small_fixtures)

    # Then I get no error
    assert 0 == exit_code
