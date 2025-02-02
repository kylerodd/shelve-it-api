from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from db import get_session
from models.container import Container
from crud import container as repo

router = APIRouter()

@router.post("/container/")
def create_container(container: Container, session = Depends(get_session)) -> Container:
    if container.parent_id is not None:
        parent_container = repo.find_by_id(container.parent_id, session)
        if parent_container is None:
            raise HTTPException(status_code=500, detail="Invalid parent container")
    return repo.add(container, session)


@router.get("/container/")
def get_containers(
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    session: Session = Depends(get_session)
) -> list[Container]:
    return repo.find_page(offset, limit, session)


@router.get("/container/{container_id}")
def find_container(container_id: int, session = Depends(get_session)) -> Container:
    container = repo.find_by_id(container_id, session)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    return container


@router.delete("/containers/{container_id}")
def delete_container(container_id: int, session = Depends(get_session)):
    container = repo.find_by_id(container_id, session)
    if not container:
        raise HTTPException(status_code=404, detail="Container not found")
    repo.delete(container)
    return {"ok": True}

