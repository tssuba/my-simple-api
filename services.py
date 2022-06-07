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


async def create_article(db: orm.SessionLocal, article: _schemas.ArticleCreate):
    article = _models.Article(**article.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    return _schemas.Article.from_orm(article)


async def get_articles(db: _orm.SessionLocal):
    pass