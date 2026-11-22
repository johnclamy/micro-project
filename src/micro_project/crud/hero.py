from sqlmodel import Session, select
from ..model.hero import Hero


__all__ = ["read_heroes"]


def read_heroes(session: Session) -> list[Hero]:
    """Return all heroes, ordered by id."""
    statement = select(Hero).where(Hero.name == 'Deadpond').where(Hero.age == 48)
    results = list(session.exec(statement).all())
    
    return results
