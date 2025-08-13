from datetime import datetime
from uuid import UUID

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.domain.entities.file_id import FileId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.user import NameDisplay
from app.domain.entities.user_id import UserId


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


class WorkModel(Base):
    """Модель работы витрины."""

    __tablename__ = "works"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    showcase_id: Mapped[UUID] = mapped_column(ForeignKey("showcases.id"))
    title: Mapped[str]
    description: Mapped[str]
    file_path: Mapped[FileId]


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
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str]
    nickname: Mapped[str | None] = mapped_column(nullable=True)
    password: Mapped[str]
    photo: Mapped[FileId | None] = mapped_column(nullable=True)
    description: Mapped[str]
    status: Mapped[str | None] = mapped_column(nullable=True)

    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id"))
    communication_method_id: Mapped[UUID] = mapped_column(
        ForeignKey("communication_methods.id")
    )
    showcase_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("showcases.id"), nullable=True
    )
    name_display: Mapped[NameDisplay | None] = mapped_column(
        Enum(NameDisplay), default=NameDisplay.USERNAME, nullable=True
    )

    tags: Mapped[list[TagModel]] = relationship(
        TagModel, secondary=UserTagModel.__table__
    )
    specializations: Mapped[list[SpecializationModel]] = relationship(
        SpecializationModel, secondary=UserSpecializationModel.__table__
    )


class LikeModel(Base):
    """Модель лайков."""

    __tablename__ = "likes"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[UserId] = mapped_column(ForeignKey("users.id"))
    showcase_id: Mapped[ShowcaseId] = mapped_column(ForeignKey("showcases.id"))


class SkipModel(Base):
    """Модель скипа."""

    __tablename__ = "skips"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    user_id: Mapped[UserId] = mapped_column(ForeignKey("users.id"))
    showcase_id: Mapped[ShowcaseId] = mapped_column(ForeignKey("showcases.id"))


class ChatModel(Base):
    """Модель чата между двумя пользователями."""

    __tablename__ = "chats"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    user1_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user2_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))


class ChatMessageModel(Base):
    """Модель сообщения в чате."""

    __tablename__ = "chat_messages"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    chat_id: Mapped[UUID] = mapped_column(ForeignKey("chats.id"))
    sender_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    text: Mapped[str]
    timestamp: Mapped[datetime]
