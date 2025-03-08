from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost/car_rental')

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()
result = session.execute(text("SHOW TABLES;"))
for table in result:
    print(table)
