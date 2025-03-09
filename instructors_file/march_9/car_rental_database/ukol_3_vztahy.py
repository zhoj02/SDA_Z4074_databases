from sqlalchemy.orm import sessionmaker

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()