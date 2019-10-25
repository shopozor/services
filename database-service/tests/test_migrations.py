import sh

def test_migrations_can_be_applied_without_errors():
    # 1. Check that the migration status is fine
    # assert we see the migrations folder from here

    # 2. Apply migration
    # TODO: put the endpoint in a fixture in conftest.py
    cmd = sh.Command('hasura')
    result = cmd('--skip-update-check', 'migrate', 'apply', '--endpoint', 'http://localhost:8080')

    # 3. Verify that the migration performed without errors
    assert 0 == result.exit_code