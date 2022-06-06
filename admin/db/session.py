from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "postgresql://mxqjacjonhhrii:af39c58d56c39bd7c3376ccecda1671780e9d52fedfeabd858150d1318f5a331@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/de1ad77vg2jm6i"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

current_session = scoped_session(SessionLocal)
