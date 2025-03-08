from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/')

Session = sessionmaker(bind=db)

session = Session()
session.execute(text("CREATE DATABASE car_rental"))
