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

    def __repr__(self):
        return self.barva


session = sessionmaker(db)()

print(session.query(Item).filter(Item.id==1).first())
print(session.query(Item).filter_by(id=1).first())
