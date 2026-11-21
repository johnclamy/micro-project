from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..crud.hero import read_heroes
from ..data.db import get_session
from ..model.hero import Hero


router = APIRouter(prefix="/api", tags=["heroes"])


@router.get("/heroes", response_model=list[Hero])
def get_heroes(session: Session = Depends(get_session)) -> list[Hero]:
    return read_heroes(session)
