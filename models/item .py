from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: int = Field(primary_key=True)
    container_id: int | None = Field(foreign_key="container.id")