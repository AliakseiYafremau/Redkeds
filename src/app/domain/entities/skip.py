from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from .showcase import ShowcaseId
from .user_id import UserId

SkipId = NewType("SkipId", UUID)


@dataclass
class Skip:
    """Сущность скипа (пользователь скипнул витрину)."""

    id: SkipId
    user_id: UserId
    showcase_id: ShowcaseId
