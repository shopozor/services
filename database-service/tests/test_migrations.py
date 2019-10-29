import os
import sh


def test_migrations_can_be_applied_without_errors(hasura_endpoint):
    # Given I am in the right location
    assert os.path.exists('migrations')
    assert os.path.isfile('config.yaml')

    # When I apply the migrations
    cmd = sh.Command('hasura')
    result = cmd('migrate', 'apply', '--endpoint',
                 hasura_endpoint, '--skip-update-check')

    # Then I get no errors
    assert 0 == result.exit_code
