from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Time

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/hobby_market')

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    nazev_polozky = Column(String(20))
    barva = Column(Integer, ForeignKey('barva.id'))


class Barva(Base):
    __tablename__ = 'barva'
    id = Column(Integer, primary_key=True)
    nazev = Column(String(20))
    kategorie = Column(String(20))
    hexakod = Column(String(20))

Base.metadata.drop_all(db)
Base.metadata.create_all(db)
