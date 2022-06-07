import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


# host = os.environ["POSTGRES_HOST"]
# port = os.environ["POSTGRES_PORT"]
# user = os.environ["POSTGRES_USER"]
# password = os.environ["POSTGRES_PASS"]
# db = os.environ["POSTGRES_DB"]
# dbtype = "postgresql"

# SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"

# engine = create_engine(SQLALCHEMY_DATABASE_URI)


engine = _sql.create_engine("postgresql://postgres:Tanmay123@localhost/item_db", 
    echo = True
)

SessionLocal = _orm.sessionmaker(bind = engineNews)

Base = _declarative.declarative_base()



