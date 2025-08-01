from dataclasses import dataclass

from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.file_id import FileId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId


@dataclass
class NewUserDTO:
    """DTO для создания нового пользователя."""

    email: str
    username: str
    password: str
    specialization: list[SpecializationId]
    city: CityId
    description: str
    tags: list[TagId]
    communication_method: CommunicationMethodId

    nickname: str | None = None
    photo: FileId | None = None
    status: str | None = None


@dataclass
class LoginUserDTO:
    """DTO для входа пользователя."""

    email: str
    password: str


@dataclass
class PasswordChangeDTO:
    """DTO для смены пароля пользователя."""

    old_password: str
    new_password: str


@dataclass
class UserDTO:
    """DTO для чтения пользователя."""

    email: str
    username: str
    nickname: str | None = None
    photo: FileId | None = None
    specialization: list[SpecializationId] | None = None
    city: CityId | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None


@dataclass
class UpdateUserDTO:
    """DTO для обновления пользователя."""

    email: str | None = None
    username: str | None = None
    nickname: str | None = None
    photo: FileId | None = None
    specialization: list[SpecializationId] | None = None
    city: CityId | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None
