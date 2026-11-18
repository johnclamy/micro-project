from pathlib import Path
from sqlmodel import SQLModel, create_engine
from ..model.hero import Hero


__all__ = ["Hero", "create_db_and_tables", "engine"]


DATABASE_PATH = Path(__file__).resolve().parent / "database.db"
SQLITE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"


engine = create_engine(SQLITE_URL)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)
