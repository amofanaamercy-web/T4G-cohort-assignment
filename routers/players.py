from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
import repositories
import schemas

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


@router.post(
    "/",
    response_model=schemas.PlayerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_player(
    player: schemas.PlayerCreate,
    db: Session = Depends(get_db)
):
    existing_player = repositories.get_player_by_email(
        db,
        player.email
    )

    if existing_player:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return repositories.create_player(db, player)


@router.get(
    "/",
    response_model=list[schemas.PlayerResponse]
)
def get_players(
    db: Session = Depends(get_db)
):
    return repositories.get_players(db)


@router.get(
    "/{player_id}",
    response_model=schemas.PlayerResponse
)
def get_player(
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

    return player


@router.put(
    "/{player_id}",
    response_model=schemas.PlayerResponse
)
def update_player(
    player_id: int,
    player_data: schemas.PlayerUpdate,
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

    if player_data.email:
        existing_email = repositories.get_player_by_email(
            db,
            player_data.email
        )

        if existing_email and existing_email.id != player_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    return repositories.update_player(
        db,
        player_id,
        player_data
    )


@router.delete(
    "/{player_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_player(
    player_id: int,
    db: Session = Depends(get_db)
):
    player = repositories.delete_player(
        db,
        player_id
    )

    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )

    return None