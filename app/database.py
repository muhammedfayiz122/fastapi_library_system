from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# Loads .env file so you can use environment variables.
load_dotenv()

# Gets your DB connection string.
DATABASE_URL = os.getenv('DATABASE_URL')

# Core object that connects to the DB.
engine = create_engine(DATABASE_URL)

# Manages database sessions per request.
SessionLocal = sessionmaker(autocommit=False,autoflush =False,bind = engine)

# Base class for defining ORM models (like Book, Author).a
Base = declarative_base()

# Used in routes via dependency injection (Depends(get_db)).
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()