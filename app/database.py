from sqlalchemy.orm import sessionmaker , declarative_base
from sqlalchemy import create_engine

DB_URl="sqlite:///./users.db"

engine=create_engine(DB_URl)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base= declarative_base()