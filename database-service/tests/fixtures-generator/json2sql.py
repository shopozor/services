import json_helpers

import argparse
import datetime
import os


def timestamp():
    # this generates the same kind of timestamps as hasura does for its migration files
    epoch = datetime.datetime.utcfromtimestamp(0)
    now = datetime.datetime.now()
    return round((now - epoch).total_seconds() * 1000)

def generate_up_migration(json_data, output_folder, migration_name, write_mode):
    migration_file = os.path.join(output_folder, migration_name + '.up.sql')
    with open(migration_file, write_mode) as output_file:
        for table, data in json_data.items():
            for data_item in data:
                columns = ','.join(data_item.keys())
                values = ','.join(
                    map(lambda val: f"'{val}'", data_item.values()))
                output_file.write(
                    f'INSERT INTO public.{table} ({columns}) VALUES ({values});\n')

def generate_down_migration(json_data, output_folder, migration_name, write_mode):
    migration_file = os.path.join(output_folder, migration_name + '.down.sql')
    with open(migration_file, write_mode) as output_file:
        for table in json_data.keys():
            output_file.write(f'DELETE FROM public.{table};\n')


def main(input, migration_name, output_folder, write_mode):
    json_data = json_helpers.load(input)
    migration_file_format = f'{timestamp()}_{migration_name}'
    generate_up_migration(json_data, output_folder, migration_file_format, write_mode)
    generate_down_migration(json_data, output_folder, migration_file_format, write_mode)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Converts json fixtures to sql script')
    parser.add_argument('-i', '--input', type=str,
                        help='Input json fixtures file')
    parser.add_argument('-n', '--migration-name', type=str,
                        help='Hasura migration name')
    parser.add_argument('-o', '--output-folder', type=str, default='.',
                        help='Folder the migration should be copied to')
    parser.add_argument('-m', '--write-mode', type=str,
                        default='w', help='(w)rite or (a)ppend')
    args = parser.parse_args()

    main(args.input, args.migration_name, args.output_folder, args.write_mode)
