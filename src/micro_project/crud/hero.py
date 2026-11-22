from typing import cast


from sqlmodel import Session, col, select
from ..model.hero import Hero


__all__ = ["read_heroes"]


def read_heroes(session: Session) -> list[Hero]:
    """Return all heroes, ordered by id."""
    statement = select(Hero).order_by(col(Hero.id))
    results = list(session.exec(statement).all())

    return results


def read_experienced_heroes(session: Session) -> list[Hero]:
    """Return all heroes that are older than 35, ordered by age."""
    statement = select(Hero).where(cast(int, Hero.age) > 35).order_by(col(Hero.age))
    results = list(session.exec(statement).all())

    return results
