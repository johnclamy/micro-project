import uvicorn


__all__ = ["main"]


def main() -> None:
    uvicorn.run(
        "micro_project.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
