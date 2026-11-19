from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    """Persisted hero record."""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=100)
    secret_name: str = Field(min_length=1, max_length=255)
    age: int | None = Field(default=None, ge=0)
