from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False, unique = True)


#return string representation in console
def __repr__(self):
    return f"<Item name = {self.name}>"
