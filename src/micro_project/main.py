import uvicorn
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from fastapi import FastAPI
from micro_project.data.db import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    create_db_and_tables()
    yield


app = FastAPI(
    title="Micro Project",
    lifespan=lifespan,
)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "micro_project.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
