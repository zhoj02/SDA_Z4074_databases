# Ukoly
from sqlalchemy.orm import sessionmaker

# Ukol c.1 - Vloz do database 3 klienty

# Ukol c.2 - Vloz do database 10 transakci

from database_definition_bank import Transactions, db, Clients

Session = sessionmaker(bind=db)
session = Session()

clients = [
    {"name": "Jan", "surname": "Zhouf", "city": "Prague"},
    {"name": "Jan", "surname": "Marek", "city": "Kolín"},
    {"name": "Petr", "surname": "Malý", "city": "Bratislava"},
]

transactions = [
    {"date": "2022-07-10 14:00:00", "amount": 1},
    {"date": "2022-07-11 13:00:00", "amount": 200},
    {"date": "2022-08-10 18:00:00", "amount": 200},
    {"date": "2022-09-10 14:00:00", "amount": 500},
    {"date": "2022-07-10 14:00:00", "amount": 2800},
    {"date": "2022-10-10 19:00:00", "amount": 20550},
    {"date": "2022-07-10 14:00:00", "amount": 200},
    {"date": "2022-10-10 17:00:00", "amount": 200},
    {"date": "2022-10-10 14:00:00", "amount": 547},
    {"date": "2022-10-11 14:00:00", "amount": 200},
]

for client in clients:
    session.add(Clients(**client))
    session.commit()

for transaction in transactions:
    session.add(Transactions(**transaction))
    session.commit()


