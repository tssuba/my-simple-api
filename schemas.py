import pydantic as _pydantic

class _ArticleBase(_pydantic.BaseModel):
    published_date:str
    link:str
    publisher:str
    title:str


class ArticleCreate(_ArticleBase):
    pass


class Article(_ArticleBase):
    id: int

    class Config:
        orm_mode = True