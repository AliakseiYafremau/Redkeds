from dataclasses import dataclass
from typing import NewType

LikeId = NewType("LikeId", int)


@dataclass
class Like:
    """Сущность лайка пользователя на витрину."""

    id: LikeId | None
    user_id: int
    showcase_id: int
