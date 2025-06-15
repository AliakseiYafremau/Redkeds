from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from .user_id import UserId

ShowcaseId = NewType("ShowcaseId", UUID)
WorkId = NewType("WorkId", UUID)
WorkFileId = NewType("WorkFileId", UUID)


@dataclass
class Showcase:
    """Сущность витрины пользователя.

    Витрина содержит работы пользователя, которые он хочет показать
    другим пользователям.
    """

    id: ShowcaseId | None
    owner_id: UserId


@dataclass
class Work:
    """Сущность работы в витрине пользователя."""

    id: WorkId | None
    showcase_id: ShowcaseId
    title: str
    description: str


@dataclass
class WorkFile:
    """Сущность файла работы в витрине пользователя."""

    id: WorkFileId | None
    work_id: WorkId
    file_path: str
