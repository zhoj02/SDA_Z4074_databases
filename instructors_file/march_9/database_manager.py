class DatabaseManager:
    def __init__(
            self,
            database_name,
            database_server,
            database_user,
            database_password,
    ):
        ...

    def connect(self):
        ...

    def select(self, select):
        ...

    def insert(self, data, table_name):
        ...
