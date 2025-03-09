from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Time

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/bank')

Base = declarative_base()


class Transactions(Base):
    __tablename__ = 'transactions'

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Time, nullable=False)
    amount = Column(Integer, nullable=False)


class Clients(Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)


Base.metadata.create_all(db)
