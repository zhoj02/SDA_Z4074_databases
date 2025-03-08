from sqlalchemy.orm import sessionmaker
from database_definition import Cars, Clients, db

Session = sessionmaker(bind=db)
session = Session()

for client in session.query(Clients).all():
    print(client)

for car in session.query(Cars).all():
    print(car)