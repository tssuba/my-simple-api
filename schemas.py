import pydantic as _pydantic

class _ArticleBase(_pydantic.BaseModel):
    link: str
    published_date = str
    publisher = str
    title = str


class ArticleCreate(_ArticleBase):
    pass


class Article(_ArticleBase):
    id: int

    class Config:
        orm_mode = True