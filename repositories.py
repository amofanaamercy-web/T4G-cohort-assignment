from sqlalchemy.orm import Session

import models
import schemas


# -------------------------
# PLAYER REPOSITORY
# -------------------------

def create_player(db: Session, player: schemas.PlayerCreate):
    new_player = models.Player(
        name=player.name,
        email=player.email
    )

    db.add(new_player)
    db.commit()
    db.refresh(new_player)

    return new_player


def get_players(db: Session):
    return db.query(models.Player).all()


def get_player_by_id(db: Session, player_id: int):
    return db.query(models.Player).filter(
        models.Player.id == player_id
    ).first()


def get_player_by_email(db: Session, email: str):
    return db.query(models.Player).filter(
        models.Player.email == email
    ).first()


def update_player(
    db: Session,
    player_id: int,
    player_data: schemas.PlayerUpdate
):
    player = get_player_by_id(db, player_id)

    if not player:
        return None

    if player_data.name is not None:
        player.name = player_data.name

    if player_data.email is not None:
        player.email = player_data.email

    db.commit()
    db.refresh(player)

    return player


def delete_player(db: Session, player_id: int):
    player = get_player_by_id(db, player_id)

    if not player:
        return None

    db.delete(player)
    db.commit()

    return player


# -------------------------
# GAME REPOSITORY
# -------------------------

def create_game(
    db: Session,
    player_id: int,
    secret_number: int
):
    new_game = models.Game(
        player_id=player_id,
        secret_number=secret_number,
        attempts=0,
        status="playing"
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game


def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(
        models.Game.id == game_id
    ).first()


def get_games_by_player(db: Session, player_id: int):
    return db.query(models.Game).filter(
        models.Game.player_id == player_id
    ).all()


def save_game(db: Session, game: models.Game):
    db.commit()
    db.refresh(game)

    return game


def delete_game(db: Session, game_id: int):
    game = get_game_by_id(db, game_id)

    if not game:
        return None

    db.delete(game)
    db.commit()

    return game