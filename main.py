from typing import Annotated


from fastapi import FastAPI
from sqlmodel import select

from db import lifespan, SessionDep
from models.container import Container
from routers import container as containerRouter;

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(containerRouter.router)

# Test
@app.post("/prepop/")
def create_container(session: SessionDep) -> None:
    toDelete = session.exec(select(Container))
    for container in toDelete: 
        session.delete(container)
        session.commit()
    grandpa = Container(name="grandpa")
    session.add(grandpa)
    session.commit()
    session.refresh(grandpa)
    dad = Container(name="dad", parent_id=grandpa.id)
    session.add(dad)
    session.commit()
    session.refresh(dad)
    child = Container(name="child", parent_id=dad.id)
    session.add(child)
    session.commit()
    session.refresh(child)
    grandChild = Container(name="grandChild", parent_id=child.id)
    session.add(grandChild)
    session.commit()
    session.refresh(grandChild)
    