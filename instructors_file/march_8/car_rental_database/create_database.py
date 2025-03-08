from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

with open("moje_heslo.txt", 'r') as file:
    password = file.read()

db = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/')

Session = sessionmaker(bind=db)

session = Session()
session.execute(text("CREATE DATABASE car_rental"))
