import os.path


def get_query_from_file(graphql_calls_folder, query_name):
    path_to_query = os.path.join(graphql_calls_folder, f'{query_name}.graphql')
    with open(path_to_query, 'r') as myfile:
        return myfile.read().replace('\n', '')
