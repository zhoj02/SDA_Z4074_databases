from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, func, text
from sqlalchemy import and_

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()
smt = text("SELECT booking_id FROM bookings WHERE total_amount > :amount")
result = session.query(Bookings).from_statement(smt).params(amount=200).all()
print(result)

