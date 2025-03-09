from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

#1
result = session.query(Bookings).filter(Bookings.client_id==3)
for booking in result:
    print(booking)

#2
select = select(Bookings)
conn = db.connect()
result = conn.execute(select).fetchall()
print(result)


