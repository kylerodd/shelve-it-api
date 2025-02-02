from sqlalchemy import Index, UniqueConstraint
from sqlmodel import Field, SQLModel


class Container(SQLModel, table=True):
    id: int = Field(primary_key=True)
    parent_id: str  | None = Field(foreign_key="container.id", default=None, nullable=True)
    name: str
    __table_args__ = (
        UniqueConstraint("parent_id", "name", name="unique_name_parent"),
    )


