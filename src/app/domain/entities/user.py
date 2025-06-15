from dataclasses import dataclass

from .communication_method import CommunicationMethodId
from .showcase import ShowcaseId
from .specialization import SpecializationId
from .tag import TagId
from .user_id import UserId


@dataclass
class User:
    """Сущность пользователя."""

    id: UserId | None
    username: str
    password: str
    photo: str | None
    specialization: list[SpecializationId]
    city: str | None
    description: str
    tags: list[TagId]
    connection_method: CommunicationMethodId
    status: str | None  # Состояние пользователя
    showcase: ShowcaseId | None
