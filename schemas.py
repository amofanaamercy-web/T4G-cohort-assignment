from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class PlayerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr


class PlayerUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None


class PlayerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class GameCreate(BaseModel):
    player_id: int


class GuessRequest(BaseModel):
    guess: int = Field(ge=1, le=50)


class GameResponse(BaseModel):
    id: int
    player_id: int
    attempts: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True