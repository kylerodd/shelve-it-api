from sqlmodel import Field, SQLModel


class Item(SQLModel, table=True):
    id: int = Field(primary_key=True)
    container_id: int | None = Field(foreign_key="container.id")
    checked_out: bool
    description: str | None= Field(default= None)