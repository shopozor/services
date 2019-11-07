import os
import sh


class HasuraClient:
    def __init__(self, hasura_endpoint):
        self.__cli = sh.Command('hasura')
        self.__endpoint = hasura_endpoint

    def apply_migrations(self, migrations_folder):
        result = self.__cli('migrate', 'apply', '--endpoint', self.__endpoint,
                            '--project', migrations_folder, '--skip-update-check')
        return result.exit_code

    def __get_number_of_migrations_in_folder(self, folder):
        return int(len(os.listdir(folder)) / 2)

    def rollback_migrations(self, project_folder):
        migrations_folder = os.path.join(project_folder, 'migrations')
        nb_migrations = self.__get_number_of_migrations_in_folder(
            migrations_folder)
        result = self.__cli('migrate', 'apply', '--down', nb_migrations, '--endpoint',
                            self.__endpoint, '--project', project_folder, '--skip-update-check')
        return result.exit_code
