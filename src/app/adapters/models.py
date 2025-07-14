from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey


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


class SpecializationModel(Base):
    """Модель специальности."""

    __tablename__ = "specializations"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]


class ShowcaseModel(Base):
    """Модель витрины."""

    __tablename__ = "showcases"

    id: Mapped[UUID] = mapped_column(primary_key=True)


class CommunicationMethodModel(Base):
    """Модель предпочтения способа общения."""

    __tablename__ = "communication_methods"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]


class UserModel(Base):
    """Модель пользователя."""

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    photo: Mapped[str | None]
    description: Mapped[str]
    status: Mapped[str]

    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id"))
    communication_method_id: Mapped[UUID] = mapped_column(ForeignKey("communication_methods.id"))
    showcase_id: Mapped[UUID] = mapped_column(ForeignKey("showcases.id"))


class UserTagModel(Base):
    """Связь пользователей с их тегами."""

    __tablename__ = "user_tag"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    tag_id: Mapped[UUID] = mapped_column(ForeignKey("tags.id"))


class UserSpecializationModel(Base):
    """Связь пользователей с их специализациями."""

    __tablename__ = "user_specialization"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    specialization_id: Mapped[UUID] = mapped_column(ForeignKey("specializations.id"))
