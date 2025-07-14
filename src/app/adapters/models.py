from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовая модель в базе данных."""


class TagModel(Base):
    """Модель тега."""

    __tablename__ = "tables"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]


class CityModel(Base):
    """Модель города."""

    __tablename__ = "cities"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
