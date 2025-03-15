from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Time

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/bank')

Base = declarative_base()
select_test = "SELECT 1;"
Session = sessionmaker(db)
session = Session()

print(session.execute(text(select_test)).all())