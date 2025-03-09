from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select, func
from sqlalchemy import and_

from instructors_file.march_8.car_rental_database.database_definition import Cars, Bookings, Clients, db

Session = sessionmaker(bind=db)
session = Session()

bookings = (
    session
    .query(Bookings.client_id, func.sum(Bookings.total_amount))
    .filter(
        and_(Bookings.start_date >= '2020-07-10', Bookings.end_date <= '2020-07-17')
    )
    .group_by(Bookings.client_id)
)
for booking in bookings:
    print(booking)

"""
SELECT sum(booking_amount) from bookings group by client_id
"""
"""
client_id, booking_amount
1, 1000
1, 1200
2,1700
1,2000
2, 1500
1,8000
"""

"""
client_id, booking_amount
1, 1000
1, 1200
1,2000
1,8000


2, 1700
2, 1500

"""