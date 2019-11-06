class DatabaseHandler:
    def __init__(self, connection):
        self.__conn = connection

    def __get_tables_list(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        return [item[0] for item in cursor.fetchall()]

    def is_database_empty(self):
        tables_list = self.__get_tables_list()
        return 0 == len(tables_list)

    def get_non_empty_tables(self):
        cursor = self.__conn.cursor()
        tables_list = self.__get_tables_list()
        tables_stats = {}
        for table in tables_list:
            cursor.execute(f'SELECT COUNT(*) FROM {table}')
            nb_entries = cursor.fetchall()
            tables_stats[table] = nb_entries[0][0]
        return sorted(tuple(item for item in tables_stats if tables_stats[item] > 0))