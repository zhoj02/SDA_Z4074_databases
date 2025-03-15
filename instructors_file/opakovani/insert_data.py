from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Time

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/hobby_market')

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    nazev_polozky = Column(String(20))
    barva_id = Column(Integer, ForeignKey('barva.id'))
    barva = relationship("Barva")


class Barva(Base):
    __tablename__ = 'barva'
    id = Column(Integer, primary_key=True)
    nazev = Column(String(20))
    kategorie = Column(String(20))
    hexakod = Column(String(20))


session = sessionmaker(db)()

session.add_all(
    [
    Item(id=1, nazev_polozky="pila na hrebiky"),
    Item(id=2, nazev_polozky="pila na cihly"),
    ]
)
session.commit()