from mysql.connector import connect

select = "SHOW TABLES"

with connect(user='root', password='YourNewPassword', database='mysql') as conn:
    with conn.cursor() as cursor:
        cursor.execute(select)
        print(cursor.fetchall())
