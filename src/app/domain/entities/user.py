from dataclasses import dataclass
from enum import Enum
from typing import Any

from .city import CityId
from .communication_method import CommunicationMethodId
from .file_id import FileId
from .showcase import ShowcaseId
from .specialization import SpecializationId
from .tag import TagId
from .user_id import UserId


class NameDisplay(Enum):
    """Выбор отображения пользователя."""

    USERNAME = "username"
    NICKNAME = "nickname"


@dataclass
class User:
    """Сущность пользователя."""

    id: UserId
    email: str
    username: str
    nickname: str | None
    name_display: NameDisplay
    password: str
    photo: FileId | None
    default_photo: FileId | None
    specialization: list[SpecializationId]
    city: CityId
    description: str
    tags: list[TagId]
    communication_method: CommunicationMethodId
    status: str | None  # Состояние пользователя
    showcase: ShowcaseId | None

    def __post_init__(self) -> None:
        self._check_invariant()

    def __setattr__(self, name: Any, value: Any) -> None:
        super().__setattr__(name, value)
        self._check_invariant()

    def _check_invariant(self):
        if (
            hasattr(self, "nickname")
            and hasattr(self, "name_display")
            and self.name_display is NameDisplay.NICKNAME
            and self.nickname is None
        ):
            raise ValueError("Пользователь не может отображать nickname, если его нет.")
        if (
            hasattr(self, "photo")
            and hasattr(self, "default_photo")
            and self.photo is not None
            and self.default_photo is not None
        ):
            raise ValueError(
                "Пользователь не может иметь и фото, и фото по умолчанию одновременно."
            )
