from typing import List, Dict, Union
from GoogleNewsScaper import GoogleNewsArticle, GoogleNewsScraper
from RecentJournalsScaper import ResearchArticle, RecentJournalsScraper
from models import Article, ResearchArticle,  Item

import fastapi as _fastapi
import datetime as _dt
import sqlalchemy.orm as _orm

import database as _database, models as _models, schemas as _schemas


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_article(db: _orm.Session, article: _schemas.ArticleCreate):
    article = _models.Article(**article.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    return _schemas.Article.from_orm(article)


async def fetch_articles(db: _orm.Session, articles: List[GoogleNewsArticle]):

    obj_list = []
    data_list = articles
    for record in data_list:
        data_obj = _models.Article(**record)
        obj_list.append(data_obj)
    db.add_all(obj_list)
    db.commit()
    news = db.query(_models.Article)
    return list(map(_schemas.Article.from_orm, news))


async def fetch_research_articles(db: _orm.Session, articles: List[ResearchArticle]):

    obj_list = []
    data_list = articles
    for record in data_list:
        data_obj = _models.ResearchArticle(**record)
        obj_list.append(data_obj)
    db.add_all(obj_list)
    db.commit()
    research = db.query(_models.ResearchArticle)
    return list(map(_schemas.ResearchArticle.from_orm, research))


async def get_articles(db: _orm.Session):
    # query = Article.select().order_by(Article.c.id.desc()).limit(25)
    articles = db.query(_models.Article).order_by(Article.id.desc()).limit(25)

    return list(map(_schemas.Article.from_orm, articles))


async def get_research_articles(db: _orm.Session):
    # query = Article.select().order_by(Article.c.id.desc()).limit(25)
    articles = db.query(_models.ResearchArticle).order_by(ResearchArticle.id.desc()).limit(25)

    return list(map(_schemas.ResearchArticle.from_orm, articles))


async def delete_all_articles(db: _orm.Session):
    articles = db.query(_models.Article)

    articles.delete()
    db.commit()


async def delete_all_research_articles(db: _orm.Session):
    articles = db.query(_models.ResearchArticle)

    articles.delete()
    db.commit()