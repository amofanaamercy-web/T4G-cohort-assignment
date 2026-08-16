from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    games = relationship(
        "Game",
        back_populates="player",
        cascade="all, delete-orphan"
    )


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)

    secret_number = Column(Integer, nullable=False)
    attempts = Column(Integer, default=0)
    status = Column(String(20), default="playing")
    created_at = Column(DateTime, default=datetime.utcnow)

    player = relationship(
        "Player",
        back_populates="games"
    )