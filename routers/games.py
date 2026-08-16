import random

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
import repositories
import schemas

router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.post(
    "/",
    response_model=schemas.GameResponse,
    status_code=status.HTTP_201_CREATED
)
def start_game(
    game_data: schemas.GameCreate,
    db: Session = Depends(get_db)
):
    player = repositories.get_player_by_id(
        db,
        game_data.player_id
    )

    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )

    secret_number = random.randint(1, 50)

    return repositories.create_game(
        db,
        game_data.player_id,
        secret_number
    )


@router.get(
    "/{game_id}",
    response_model=schemas.GameResponse
)
def get_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = repositories.get_game_by_id(
        db,
        game_id
    )

    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return game


@router.post("/{game_id}/guess")
def make_guess(
    game_id: int,
    guess_data: schemas.GuessRequest,
    db: Session = Depends(get_db)
):
    game = repositories.get_game_by_id(
        db,
        game_id
    )

    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    if game.status == "won":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This game has already been won"
        )

    game.attempts += 1

    if guess_data.guess < game.secret_number:
        message = "Too low!"

    elif guess_data.guess > game.secret_number:
        message = "Too high!"

    else:
        message = "Correct!"
        game.status = "won"

    repositories.save_game(db, game)

    return {
        "message": message,
        "attempts": game.attempts,
        "status": game.status
    }


@router.get(
    "/player/{player_id}",
    response_model=list[schemas.GameResponse]
)
def get_player_games(
    player_id: int,
    db: Session = Depends(get_db)
):
    player = repositories.get_player_by_id(
        db,
        player_id
    )

    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )

    return repositories.get_games_by_player(
        db,
        player_id
    )


@router.delete(
    "/{game_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = repositories.delete_game(
        db,
        game_id
    )

    if not game:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Game not found"
        )

    return None