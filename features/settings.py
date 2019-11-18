
import os

GRAPHQL_RESPONSES_DIR = os.path.join('..', 'graphql', 'responses')


def json_fixtures_dir(context):
    return os.path.join('..', 'fixtures', context.userdata.get('fixtures_set'))


def graphql_responses_dir(context):
    return os.path.join(GRAPHQL_RESPONSES_DIR, context.userdata.get('fixtures_set'))
