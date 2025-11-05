# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager

# when you start and stop the server, you’ll see those log messages in the console
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    print("🚀 Application startup")
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
