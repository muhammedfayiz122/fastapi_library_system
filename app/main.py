# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine,Base
from sqlalchemy import text

# when you start and stop the server, you’ll see those log messages in the console
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("🚀 Application startup")
    try:
        # create tables
        Base.metadata.create_all(bind=engine)
        print("table created successfully")
        # with engine.connect() as conn:
        #     conn.execute(text('Select 1'))
        #     print("Database connection successfull")
    except Exception as e:
        # print("Database connection failed")
        print("error creating tables")
    yield
    # Shutdown actions
    print("🛑 Application shutdown")

    
# Create FastAPI instance
app = FastAPI(
    title="Library Management System API",
    description="A FastAPI backend for managing books, authors, and borrow operations.",
    version="1.0.0",
    lifespan=lifespan  # 👈 modern startup/shutdown management

)



# Root route to test server
@app.get("/")
def read_root():
    return {"message": "📚 Library Management API is running successfully!"}
