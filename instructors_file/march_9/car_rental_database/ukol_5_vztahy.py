import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy import and_

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

bookings = session.query(Clients.client_id, Clients.name, Bookings.total_amount).join(Clients).filter(
    and_(Bookings.total_amount > 1100, Bookings.start_date >= '2020-07-14'))

"""
Id, jmeno zakaznika, castku za pujceni
"""