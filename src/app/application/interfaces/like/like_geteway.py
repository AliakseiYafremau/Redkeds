from typing import Protocol

from app.domain.entities.like import Like, LikeId


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

class IdProvider(Protocol):
    """Интерфейс для получения идентификатора."""

    def __call__(self) -> LikeId:
        """Возвращает ID лайка."""
        ...
