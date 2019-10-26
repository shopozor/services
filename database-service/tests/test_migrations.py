import sh

def test_migrations_can_be_applied_without_errors():
    # 1. Check that the migration status is fine
    # assert we see the migrations folder from here

    # TODO: put the endpoint in a fixture in conftest.py
    cmd = sh.Command('hasura')
    result = cmd('migrate', 'apply', '--endpoint', 'http://graphql-engine:8080', '--skip-update-check')

    assert 0 == result.exit_code