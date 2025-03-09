from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

bookings = session.query(Bookings)
for booking in bookings:
    print(bookings)
"""
Vysledek:
1, Jan Kowalski, 1200
"""
