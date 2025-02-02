from sqlmodel import select
from db import SessionDep
from models.container import Container


def find_by_id(id: int, session: SessionDep) -> Container:
    return session.get(Container, id)

def find_page(offset: int, limit: int, session: SessionDep) -> list[Container]:
    return session.exec(select(Container).offset(offset).limit(limit)).all()

def add(container: Container, session: SessionDep) -> Container:
    session.add(container)
    session.commit()
    session.refresh(container)
    return container

def delete(container: Container, session: SessionDep): 
    session.delete(container)
    session.commit()