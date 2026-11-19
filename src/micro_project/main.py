import os
import uvicorn
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from micro_project.data.db import create_db_and_tables


__all__ = ["app"]


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    create_db_and_tables()
    yield


app = FastAPI(
    title="Micro Project",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/health", tags=["meta"])
async def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "micro_project.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
