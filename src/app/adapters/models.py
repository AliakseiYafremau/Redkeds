from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Базовая модель в базе данных."""


class TagModel(Base):
    """Модель тега."""

    __tablename__ = "tags"

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


class UserTagModel(Base):
    """Связь пользователей с их тегами."""

    __tablename__ = "user_tag"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    tag_id: Mapped[UUID] = mapped_column(ForeignKey("tags.id"), primary_key=True)


class UserSpecializationModel(Base):
    """Связь пользователей с их специализациями."""

    __tablename__ = "user_specialization"

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    specialization_id: Mapped[UUID] = mapped_column(
        ForeignKey("specializations.id"), primary_key=True
    )


class UserModel(Base):
    """Модель пользователя."""

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    photo: Mapped[str | None] = mapped_column(nullable=True)
    description: Mapped[str]
    status: Mapped[str | None] = mapped_column(nullable=True)

    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id"))
    communication_method_id: Mapped[UUID] = mapped_column(
        ForeignKey("communication_methods.id")
    )
    showcase_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("showcases.id"), nullable=True
    )

    tags: Mapped[list[TagModel]] = relationship(
        TagModel, secondary=UserTagModel.__table__
    )
    specializations: Mapped[list[SpecializationModel]] = relationship(
        SpecializationModel, secondary=UserSpecializationModel.__table__
    )
