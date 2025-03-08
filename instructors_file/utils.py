from mysql.connector import connect


def select_to_database(select: str):
    with connect(user='root', password='YourNewPassword', database='mysql') as conn:
        with conn.cursor() as cursor:
            cursor.execute(select)
            return cursor.fetchall()
