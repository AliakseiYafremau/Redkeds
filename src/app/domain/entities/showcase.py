from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from .user_id import UserId

ShowcaseId = NewType("ShowcaseId", UUID)
WorkId = NewType("WorkId", UUID)


@dataclass
class Showcase:
    """Сущность витрины пользователя.

    Витрина содержит работы пользователя, которые он хочет показать
    другим пользователям.
    """

    id: ShowcaseId
    owner_id: UserId


@dataclass
class Work:
    """Сущность работы в витрине пользователя."""

    id: WorkId | None
    showcase_id: ShowcaseId
    title: str
    description: str
    file_path: str
