class DatabaseHandler:
    def __init__(self, connection):
        self.__conn = connection

    def __get_tables_list(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        return cursor.fetchall()

    def is_database_empty(self):
        tables_list = self.__get_tables_list()
        return 0 == len(tables_list)

    def get_non_empty_tables(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT relname FROM pg_stat_all_tables WHERE schemaname = 'public' AND n_tup_ins > 0")
        table_names = cursor.fetchall()
        return sorted(tuple(item[0] for item in table_names))