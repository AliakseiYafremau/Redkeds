from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from .showcase import ShowcaseId
from .user_id import UserId

LikeId = NewType("LikeId", UUID)


@dataclass
class Like:
    """Сущность лайка пользователя на витрину."""

    id: LikeId | None
    user_id: UserId
    showcase_id: ShowcaseId
