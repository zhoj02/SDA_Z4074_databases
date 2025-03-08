from mysql.connector import connect

test_select = "SHOW DATABASES"

with connect(user='root', password='YourNewPassword') as conn:
    with conn.cursor() as cursor:
        cursor.execute(test_select)
        print(cursor.fetchall())
