from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATATBASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    settings.database_username,
    settings.database_password,
    settings.database_hostname,
    settings.database_port,
    settings.database_name
)
engine = create_engine(SQLALCHEMY_DATATBASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Function: Dependency generator"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
