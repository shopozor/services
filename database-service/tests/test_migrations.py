import os
import sh


def test_shopozor_structural_migrations_can_be_applied_without_errors(hasura_endpoint, app_root_folder):
    # When I apply the migrations
    cmd = sh.Command('hasura')
    result = cmd('migrate', 'apply', '--endpoint',
                 hasura_endpoint, '--project', app_root_folder, '--skip-update-check')

    # Then I get no errors
    assert 0 == result.exit_code

    # 2. --project=/app/fixtures (after they have been generated)