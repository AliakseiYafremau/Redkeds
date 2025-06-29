from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовая модель в базе данных."""


class TagModel(Base):
    """Модель тега."""

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
