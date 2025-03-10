from sqlalchemy.orm import declarative_base, sessionmaker
from database_definition import Cars, Clients, db


Base = declarative_base()

Session = sessionmaker(bind=db)
session = Session()

client_1 = Clients(name='Jan', surname='Kowalski', address='ul. Florianska 12', city='Krakow')
car_1 = Cars(producer='Seat', model='Leon', year=2016, horse_power=80, price_per_day=200)
session.add(client_1)
session.add(car_1)
session.commit()
