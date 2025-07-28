from dataclasses import dataclass

from .city import CityId
from .communication_method import CommunicationMethodId
from .file_id import FileId
from .showcase import ShowcaseId
from .specialization import SpecializationId
from .tag import TagId
from .user_id import UserId


@dataclass
class User:
    """Сущность пользователя."""

    id: UserId
    username: str
    password: str
    photo: FileId | None
    specialization: list[SpecializationId]
    city: CityId
    description: str
    tags: list[TagId]
    communication_method: CommunicationMethodId
    status: str | None  # Состояние пользователя
    showcase: ShowcaseId | None
