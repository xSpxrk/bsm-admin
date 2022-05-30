from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "postgresql://eeblqgidzghafs:7086f04865e9a290b402b1a5f2f21d881b3a8e0be9dd492667082d497862a22d@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/d1carkfnkvd1at"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

current_session = scoped_session(SessionLocal)
