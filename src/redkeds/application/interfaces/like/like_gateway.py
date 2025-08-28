from typing import Protocol

from redkeds.domain.entities.like import Like, LikeId


class LikeSaver(Protocol):
    """Интерфейс для добавления лайков."""

    async def add_like(self, like: Like) -> LikeId:
        """Добволяет лайк витрине от пользователя."""
        ...


class LikeDeleter(Protocol):
    """Интерфейс для удаления лайков."""

    async def delete_like(self, like_id: LikeId) -> None:
        """Удаляет лайк витрине от пользователя."""
        ...


class LikeReader(Protocol):
    """Интерфейс для получения лайка."""

    async def get_like_by_id(self, like_id: LikeId) -> Like:
        """Получает лайк по ID."""
        ...
