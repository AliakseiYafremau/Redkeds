from typing import Protocol

from redkeds.domain.entities.user import UserId


class IdProvider(Protocol):
    """Интерфейс для получения идентификатора."""

    def __call__(self) -> UserId:
        """Возвращает ID пользователя."""
        ...
