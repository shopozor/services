from behave import use_fixture
from behave.fixture import use_fixture_by_tag

from fixtures import login, signup, password_reset, shops_fixtures


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
    print('before_all!')
    # TODO: 1. create graphql client
    # context.test.client = ApiClient(user=AnonymousUser())
    # get the endpoint from context.config.userdata.get('graphql_endpoint')
    # TODO: 2. apply migrations
    pass
