def get_enum_values(connection, table_name, column_name):
    cursor = connection.cursor()
    cursor.execute(f'SELECT {column_name} FROM {table_name}')
    result = [item[0] for item in cursor.fetchall()]
    cursor.close()
    return result


def apply_migrations(hasura_client, project_folder):
    has_worked = hasura_client.apply_migrations(project_folder)
    assert has_worked is True


def test_pricing_modes_enum(database_project_folder, expected_pricing_modes, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    apply_migrations(hasura_client, database_project_folder)

    # When I ask for the enum values
    actual = get_enum_values(postgres_connection, 'pricing_modes', 'mode')

    # Then
    assert expected_pricing_modes.sort() == actual.sort()


def test_product_states_enum(database_project_folder, expected_product_states, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    apply_migrations(hasura_client, database_project_folder)

    # When I ask for the enum values
    actual = get_enum_values(postgres_connection, 'product_states', 'state')

    # Then
    assert expected_product_states.sort() == actual.sort()


def test_productvariant_states_enum(database_project_folder, expected_productvariant_states, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    apply_migrations(hasura_client, database_project_folder)

    # When I ask for the enum values
    actual = get_enum_values(
        postgres_connection, 'productvariant_states', 'state')

    # Then
    assert expected_productvariant_states.sort() == actual.sort()


def test_roles_enum(database_project_folder, expected_roles, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    apply_migrations(hasura_client, database_project_folder)

    # When I ask for the enum values
    actual = get_enum_values(postgres_connection, 'roles', 'role')

    # Then
    assert expected_roles.sort() == actual.sort()


def test_vat_types_enum(database_project_folder, expected_vat_types, hasura_client, postgres_connection):
    # Given I have applied the structural migrations
    apply_migrations(hasura_client, database_project_folder)

    # When I ask for the enum values
    actual = get_enum_values(postgres_connection, 'vat_types', 'type')

    # Then
    assert expected_vat_types.sort() == actual.sort()
