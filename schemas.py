import pydantic as _pydantic
from typing import Optional

class _ArticleBase(_pydantic.BaseModel):
    published_date:Optional[str] = None
    link:Optional[str] = None
    publisher:Optional[str] = None
    title:Optional[str] = None


class ArticleCreate(_ArticleBase):
    pass


class Article(_ArticleBase):
    id: int

    class Config:
        orm_mode = True


class _ResearchArticleBase(_pydantic.BaseModel):
    published_date:Optional[str] = None
    doi:Optional[str] = None
    publisher:Optional[str] = None
    title:Optional[str] = None


class ResearchArticleCreate(_ResearchArticleBase):
    pass


class ResearchArticle(_ResearchArticleBase):
    id: int

    class Config:
        orm_mode = True