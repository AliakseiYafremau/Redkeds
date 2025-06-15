from typing import Protocol

from app.domain.entities.user import User


class UserSaver(Protocol):
    """Интерфейс для сохранения пользователя."""

    def save_user(self, user: User) -> None:
        """Сохраняет обьект пользователя."""
        ...
