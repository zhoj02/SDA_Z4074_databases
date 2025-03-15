from sqlalchemy import Column, Integer, String

ORM = "Object Relational Mapping"

# Tabulka - zamestanci
# id, jmeno, prijmeni
# 1, pepa, novák
# 2, honza, janák

class Zamestnanci:
    __tablename__ = "zamestnanci"

    id = Column(Integer)
    jmeno = Column(String)
    prijmeni = Column(String)

zamestnanec_1 = Zamestnanci(id=1, jmeno="pepa", prijmeni="novak")