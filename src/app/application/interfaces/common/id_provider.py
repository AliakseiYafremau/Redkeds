from typing import Protocol

from app.domain.entities.user import UserId


class IdProvider(Protocol):
    """Интерфейс для получения идентификатора."""

    def __call__(self) -> UserId:
        """Возвращает ID пользователя."""
        ...
