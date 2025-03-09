from mysql.connector import connect


class DatabaseManager:
    def __init__(
            self,
            database_name,
            database_server,
            database_user,
            database_password,
    ):
        self.database_name = database_name
        self.database_server = database_server
        self.database_user = database_user
        self.database_password = database_password
        self._connection = self._get_connection()

    def _get_connection(self):
        return connect(user='root', password='YourNewPassword')

    def select(self, select):
        with self._connection.cursor() as cursor:
            cursor.execute(select)
            return cursor.fetchall()

    def insert(self, data, table_name):
        ...
