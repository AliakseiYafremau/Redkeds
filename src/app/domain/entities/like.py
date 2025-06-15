from dataclasses import dataclass
from typing import NewType

from .user_id import UserId
from .showcase import ShowcaseId

LikeId = NewType("LikeId", int)


@dataclass
class Like:
    """Сущность лайка пользователя на витрину."""

    id: LikeId | None
    user_id: UserId
    showcase_id: ShowcaseId
