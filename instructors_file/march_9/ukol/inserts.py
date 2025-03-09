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

for client in clients:
    session.add(Clients(**client))
    session.commit()


