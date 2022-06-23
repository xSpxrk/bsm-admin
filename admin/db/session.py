from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "postgresql://ltgwufuynhpzvg:d4c0ce45c199f82c576aed9c18a56ef9731e5c0acdaf998ac529cb9d101efafa@ec2-63-34-180-86.eu-west-1.compute.amazonaws.com:5432/d1vuoa2ak3s34"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

current_session = scoped_session(SessionLocal)
