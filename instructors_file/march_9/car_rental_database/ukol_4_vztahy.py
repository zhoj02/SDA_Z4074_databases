from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

#2
print("Verze 2")
bookings = session.query(Bookings).filter_by(client_id=5)
# result = session.query(Bookings).filter(Bookings.client_id==5)
for booking in bookings:
    print(booking.car)
print("")
print("Verze 1")

#1
clients = session.query(Clients).filter_by(client_id=5)
for client in clients:
    for booking in client.bookings:
        print(booking.car)

