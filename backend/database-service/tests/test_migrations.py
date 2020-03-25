def test_shopozor_structural_migrations_can_be_applied(hasura_client, database_project_folder):
    # Given I have structural migrations
    project_folder = database_project_folder

    # When I apply them
    has_worked = hasura_client.apply_migrations(project_folder)

    # Then I get no error
    assert has_worked is True


def test_fixtures_migrations_can_be_applied(hasura_client, database_project_folder, fixtures_set):
    # Given I've applied structural migrations
    structural_project_folder = database_project_folder
    has_worked = hasura_client.apply_migrations(structural_project_folder)
    assert has_worked is True

    # When I apply the fixtures migrations
    has_worked = hasura_client.apply_migrations(fixtures_set)

    # Then I get no error
    assert has_worked is True
