from typing import Protocol

from app.domain.entities.user_id import UserId
from app.domain.entities.showcase import ShowcaseId


class AddLike(Protocol):
    """Интерфейс для добавления лайков."""

    async def add_like(self, user_id: UserId, showcase_id: ShowcaseId) -> bool:
        """Добволяет лайк витрине от пользователя."""
        ...

    async def delete_like(self, user_id: UserId, showcase_id: ShowcaseId) -> bool:
        """Удаляет лайк витрине от пользователя."""
        ...
