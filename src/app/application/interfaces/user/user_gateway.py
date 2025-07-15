from typing import Protocol

from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


class UserSaver(Protocol):
    """Интерфейс для сохранения пользователя."""

    async def save_user(self, user: User) -> None:
        """Сохраняет обьект пользователя."""
        ...


class UserReader(Protocol):
    """Интерфейс для чтения пользователя."""

    async def get_user_by_id(self, user_id: UserId) -> User:
        """Получает пользователя по ID."""
        ...

    async def get_user_by_username(self, username: str) -> User:
        """Получает пользователя по имени."""
        ...


class UserUpdater(Protocol):
    """Интерфейс для обновления пользователя."""

    async def update_user(self, user: User) -> None:
        """Обновляет обьект пользователя."""
        ...


class UserDeleter(Protocol):
    """Интерфейс для удаления пользователя."""

    async def delete_user(self, user_id: UserId) -> None:
        """Удаляет обьект пользователя."""
        ...
