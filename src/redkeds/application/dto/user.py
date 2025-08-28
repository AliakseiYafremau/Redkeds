from dataclasses import dataclass

from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.file_id import FileId
from redkeds.domain.entities.showcase import ShowcaseId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId
from redkeds.domain.entities.user import NameDisplay
from redkeds.domain.entities.user_id import UserId


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
    name_display: NameDisplay

    nickname: str | None = None
    photo: bytes | None = None
    default_photo: FileId | None = None
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

    id: UserId
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
    name_display: NameDisplay | None = None


@dataclass
class UpdateUserDTO:
    """DTO для обновления пользователя."""

    email: str | None = None
    username: str | None = None
    nickname: str | None = None
    photo: bytes | None = None
    specialization: list[SpecializationId] | None = None
    city: CityId | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None
    name_display: NameDisplay | None = None
