from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy import and_

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

bookings = session.query(Bookings).all()
print(bookings)
