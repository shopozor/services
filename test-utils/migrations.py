import os
import re
import sh


class HasuraClient:
    def __init__(self, hasura_endpoint):
        self.__cli = sh.Command('hasura')
        self.__endpoint = hasura_endpoint

    def __get_not_present_migrations_count(self, project_folder):
        migrations_folder = os.path.join(project_folder, 'migrations')
        relevant_timestamps = [item.split('_')[0]
                               for item in os.listdir(migrations_folder)]
        statuses = self.__cli('migrate', 'status', '--endpoint', self.__endpoint,
                              '--project', project_folder, '--skip-update-check')
        result = 0
        for timestamp in relevant_timestamps:
            status = re.findall(f'^{timestamp}.*$',
                                str(statuses), re.MULTILINE)[0]
            result += status.count('Not Present')
        return result

    def apply_migrations(self, project_folder):
        result = self.__cli('migrate', 'apply', '--endpoint', self.__endpoint,
                            '--project', project_folder, '--skip-update-check')
        if result.exit_code == 0:
            return self.__get_not_present_migrations_count(project_folder) == 0
        return False

    def __get_number_of_migrations_in_folder(self, migrations_folder):
        return int(len(os.listdir(migrations_folder)) / 2)

    def rollback_migrations(self, project_folder):
        migrations_folder = os.path.join(project_folder, 'migrations')
        nb_migrations = self.__get_number_of_migrations_in_folder(
            migrations_folder)
        result = self.__cli('migrate', 'apply', '--down', nb_migrations, '--endpoint',
                            self.__endpoint, '--project', project_folder, '--skip-update-check')
        if result.exit_code == 0:
            return self.__get_not_present_migrations_count(project_folder) == nb_migrations
        return False
