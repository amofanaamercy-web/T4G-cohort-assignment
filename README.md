# Number Guessing Game REST API

## Project Description

This project extends my original Number Guessing Game mini project into a full REST API using FastAPI, SQLAlchemy, and MySQL.

Players can register, update their information, start guessing games, submit guesses, view their games, and delete records.

The system generates a random secret number between 1 and 50. Players continue guessing until they find the correct number. The API provides feedback indicating whether each guess is too high, too low, or correct.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- python-dotenv
- Uvicorn

## Project Structure

```text
t4g-cohort5-guessing-game/
│
├── routers/
│   ├── __init__.py
│   ├── players.py
│   └── games.py
│
├── database.py
├── models.py
├── schemas.py
├── repositories.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md