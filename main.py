from fastapi import FastAPI
from routers import players, games


from database import Base, engine
import models

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Number Guessing Game API",
    description="A REST API version of the Number Guessing Game mini project",
    version="1.0.0"
)

app.include_router(players.router)
app.include_router(games.router)

@app.get("/")
def home():
    return {
        "message": "Number Guessing Game API is running"
    }