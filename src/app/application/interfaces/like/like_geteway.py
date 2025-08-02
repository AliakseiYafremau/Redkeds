from typing import Protocol

from app.domain.entities.like import Like


class AddLike(Protocol):
    """Интерфейс для добавления лайков."""

    async def add_like(self, like: Like) -> None:
        """Добволяет лайк витрине от пользователя."""
        ...


class DeleteLike(Protocol):
    """Интерфейс для удаления лайков."""

    async def delete_like(self, like: Like) -> None:
        """Удаляет лайк витрине от пользователя."""
        ...
