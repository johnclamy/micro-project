from sqlmodel import Session
from ..model.hero import Hero
from .db import engine


__all__ = ["create_heroes"]


def create_heroes() -> None:
    """Insert the demo heroes. Idempotent-ish: skips if name already exists."""
    heroes = [
        Hero(name="Deadpond", secret_name="Dive Wilson"),
        Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),
        Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48),
    ]
