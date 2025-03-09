from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Date, create_engine, ForeignKey

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/car_rental')

Base = declarative_base()

class Cars(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    producer = Column(String(30), nullable=False)
    model = Column(String(30), nullable=False)
    year = Column(Integer, nullable=False)
    horse_power = Column(Integer, nullable=False)
    price_per_day = Column(Integer, nullable=False)
    bookings = relationship('Bookings', back_populates='car', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"{self.model} {self.year}"


class Clients(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    address = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    bookings = relationship('Bookings', back_populates='client', cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return f"{self.client_id}, name, surname: {self.name, self.surname}"

class Bookings(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.client_id', ondelete="CASCADE"), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.car_id', ondelete="CASCADE"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_amount = Column(Integer, nullable=False)
    client = relationship('Clients', back_populates='bookings')
    car = relationship('Cars', back_populates='bookings')

    def __repr__(self):
        return f"Booking_id: {self.booking_id}, client_id: {self.client_id}, car_id: {self.car_id}"
