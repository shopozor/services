from behave import use_fixture
from behave.fixture import use_fixture_by_tag, use_fixture
from fixtures import graphql_client, database_seed, stellar_snapshot, login, signup, password_reset, shops_fixtures


fixtures_registry = {
    'fixture.login': login,
    'fixture.signup': signup,
    'fixture.password-reset': password_reset,
    'fixture.shops': shops_fixtures
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixtures_registry)


def before_all(context):
    use_fixture(graphql_client, context)
    use_fixture(database_seed, context)


def before_scenario(context, scenario):
    use_fixture(stellar_snapshot, context)