import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

engine = create_engine('postgresql+psycopg2://postgres:WILLIAM310@localhost:5432/ezaudita')
Base = declarative_base()

SessionLocal:Session = sessionmaker(autocommit=False,autoflush=True,bind=engine)
