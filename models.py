import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _database

from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Article(_database.Base):
    __tablename__ = "articles"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    link = _sql.Column(_sql.String, index=True, default="")
    published_date = _sql.Column(_sql.String, index=True, default="")
    publisher = _sql.Column(_sql.String, index=True, default="")
    title = _sql.Column(_sql.String, index=True, default="")


class ResearchArticle(_database.Base):
    __tablename__ = "research"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    doi = _sql.Column(_sql.String, index=True, default="")
    published_date = _sql.Column(_sql.String, index=True, default="")
    publisher = _sql.Column(_sql.String, index=True, default="")
    title = _sql.Column(_sql.String, index=True, default="")


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable = False, unique = True)


#return string representation in console
def __repr__(self):
    return f"<Item name = {self.name}>"
