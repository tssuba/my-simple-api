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


async def get_articles(db: _orm.Session):
    articles = db.query(_models.Article)

    return list(map(_schemas.Article.from_orm, leads))


async def delete_all_articles(db: _orm.Session):
    articles = db.query(_models.Article)

    articles.delete()
    db.commit()