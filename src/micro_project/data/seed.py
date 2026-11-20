from sqlmodel import Session, select
from ..model.hero import Hero
from .db import engine


__all__ = ["create_heroes"]


def create_heroes() -> None:
    """Insert the demo heroes. Idempotent-ish: skips if name already exists."""
    with Session(engine) as session:
        existing_heroes = set(session.exec(select(Hero.name)).all())
        new_heroes = [
            Hero(name="Deadpond", secret_name="Dive Wilson"),
            Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
            Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
        ]

        session.add_all(h for h in new_heroes if h.name not in existing_heroes)
        session.commit()
