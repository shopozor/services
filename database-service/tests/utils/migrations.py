import os
import sh
import shutil


class HasuraClient:
    def __init__(self, hasura_endpoint):
        self.__cli = sh.Command('hasura')
        self.__endpoint = hasura_endpoint

    def apply_migrations(self, migrations_folder):
        return self.__cli('migrate', 'apply', '--endpoint', self.__endpoint, '--project', migrations_folder, '--skip-update-check')

    def __get_number_of_migrations_in_folder(self, folder):
        return int(len(os.listdir(folder)) / 2)

    def rollback_migrations(self, project_folder):
        migrations_folder = os.path.join(project_folder, 'migrations')
        nb_migrations = self.__get_number_of_migrations_in_folder(
            migrations_folder)
        return self.__cli('migrate', 'apply', '--down', nb_migrations, '--endpoint', self.__endpoint, '--project', project_folder, '--skip-update-check')


class FixturesGenerator:
    def __init__(self, app_root_folder, output_dir):
        self.__app_root_folder = app_root_folder
        self.__output_dir = output_dir
        self.__generator_cmd = sh.Command(os.path.join(app_root_folder, 'tests',
                                                       'fixtures-generator', 'entrypoint.sh'))
        self.__fixed_timestamp = "true"

    def cleanup(self):
        if os.path.isdir(self.__output_dir):
            shutil.rmtree(self.__output_dir)

    def generate(self, fixtures_set):
        self.cleanup()
        migrations_output_dir = os.path.join(self.__output_dir, 'migrations')
        return self.__generator_cmd(fixtures_set, self.__output_dir, migrations_output_dir, self.__app_root_folder, self.__fixed_timestamp)

    def project_folder(self):
        return self.__output_dir
