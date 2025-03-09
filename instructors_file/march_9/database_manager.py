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

    def connect(self):
        with connect(user='root', password='YourNewPassword') as conn:
            with conn.cursor() as cursor:
                cursor.execute(test_select)
                print(cursor.fetchall())

        ...

    def select(self, select):
        ...

    def insert(self, data, table_name):
        ...
