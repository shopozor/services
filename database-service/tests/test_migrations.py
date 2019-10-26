import sh

def test_migrations_can_be_applied_without_errors(hasura_endpoint):
    # 1. Check that the migration status is fine
    # assert we see the migrations folder from here

    cmd = sh.Command('hasura')
    result = cmd('migrate', 'apply', '--endpoint', hasura_endpoint, '--skip-update-check')

    assert 0 == result.exit_code