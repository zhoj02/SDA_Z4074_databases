from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql+mysqlconnector://root:YourNewPassword@localhost:3306/mysql')

Base = declarative_base()
Session = sessionmaker(bind=db)

session = Session()
