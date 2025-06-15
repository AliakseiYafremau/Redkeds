from dataclasses import dataclass

from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user_id import UserId


@dataclass
class NewUserDTO:
    """DTO для создания нового пользователя."""

    username: str
    password: str
    specialization: list[SpecializationId]
    description: str
    tags: list[TagId]
    communication_method: CommunicationMethodId

    photo: str | None = None
    city: str | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None


@dataclass
class LoginUserDTO:
    """DTO для входа пользователя."""

    username: str
    password: str


@dataclass
class PasswordChangeDTO:
    """DTO для смены пароля пользователя."""

    user_id: UserId
    old_password: str
    new_password: str


@dataclass
class UserDTO:
    """DTO для чтения пользователя."""

    id: UserId
    username: str
    photo: str | None = None
    specialization: list[str] | None = None
    city: str | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: str | None = None


@dataclass
class UpdateUserDTO:
    """DTO для обновления пользователя."""

    username: str | None = None
    photo: str | None = None
    specialization: list[SpecializationId] | None = None
    city: str | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None


@dataclass
class DeleteUserDTO:
    """DTO для удаления пользователя."""

    id: UserId
