from sqlmodel import Session, col, select
from ..model.hero import Hero


__all__ = ["read_heroes"]


def read_heroes(session: Session) -> list[Hero]:
    """Return all heroes, ordered by id."""
    statement = select(Hero).order_by(col(Hero.id))
    results = list(session.exec(statement).all())
    
    return results
