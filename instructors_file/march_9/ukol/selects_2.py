# Ukoly

# Ukol c.5 - Vyber transakce, které mají hodnotu nižší než medián vašich transakcí
# Ukol c.6 - Vyber transakce, které mají hodnotu nižší než průměr vašich transakcí
# Ukol c.7 - Vyber transakce, které mají hodnotu nižší než 30. quantil vašich transakcí
# Ukol c.8 - Vyber zákazníka, jehož transakce proběhla jako poslední

from sqlalchemy.orm import sessionmaker

from database_definition_bank import Transactions, db, Clients

Session = sessionmaker(bind=db)
session = Session()

all_transactions = session.query(Transactions.amount).all()
print(all_transactions)
amounts = []
for amount in all_transactions:
    amounts.append(amount[0])
print(amounts)

