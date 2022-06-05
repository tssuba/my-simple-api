from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# host = os.environ["POSTGRES_HOST"]
# port = os.environ["POSTGRES_PORT"]
# user = os.environ["POSTGRES_USER"]
# password = os.environ["POSTGRES_PASS"]
# db = os.environ["POSTGRES_DB"]
# dbtype = "postgresql"

# SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password }@{host}:{port}/{db}"

# engine = create_engine(SQLALCHEMY_DATABASE_URI)

engine = create_engine("postgresql://postgres:Tanmay123@localhost/item_db", 
    echo = True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)

