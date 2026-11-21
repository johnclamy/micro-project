from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from micro_project.data.db import create_db_and_tables
from micro_project.data.seed import create_heroes
from micro_project.routes import heroes_router


__all__ = ["app"]


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    create_db_and_tables()
    create_heroes()
    yield


app = FastAPI(
    title="Micro Project",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(heroes_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/health", tags=["meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    from micro_project.cli import main
    main()
