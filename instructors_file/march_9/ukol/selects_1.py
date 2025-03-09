# Ukoly

# Ukol c.1 - Vyber transakce, které jsou nižší než ... (vyber podle tvých transakcí)
# Ukol c.2 - Vyber transakce, které jsou vyšší než ... (vyber podle tvých transakcí)
# Ukol c.3 - Vyber transakce, které jsou starší než ... (vyber podle tvých transakcí)
# Ukol c.4 - Vyber transakce, které jsou starší než ... a mají vyšší hodnotu než ...(vyber podle tvých transakcí)
# Ukoly
from sqlalchemy.orm import sessionmaker

from database_definition_bank import Transactions, db, Clients

Session = sessionmaker(bind=db)
session = Session()

result = session.query(Transactions).filter(Transactions.amount < 1000).all()
print(result)
print()
result = session.query(Transactions).filter(Transactions.amount > 1000).all()
print(result)
print()

result = session.query(Transactions).filter(Transactions.date > "2022-08-10").all()
print(result)
print()

result = session.query(Transactions).filter(Transactions.date < "2022-08-10").all()
print(result)
print()

