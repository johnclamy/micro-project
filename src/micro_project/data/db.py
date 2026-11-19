import os
from collections.abc import Iterator
from pathlib import Path
from sqlmodel import SQLModel, Session, create_engine
from ..model.hero import Hero


__all__ = ["Hero", "create_db_and_tables", "engine", "get_session"]


DATABASE_PATH = Path(__file__).resolve().parent / "database.db"
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
SQLITE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"


# SQLite needs this because FastAPI may access the DB from multiple threads.
engine = create_engine(
    SQLITE_URL,
    echo=os.getenv("SQL_ECHO", "").lower() in {"1", "true", "yes"},
    connect_args={"check_same_thread": False},
    pool_pre_ping=True,
)


def create_db_and_tables() -> None:
    """Create all tables if they don't exist. Safe to call repeatedly."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    """FastAPI dependency that yields a DB session."""
    with Session(engine) as session:
        yield session
