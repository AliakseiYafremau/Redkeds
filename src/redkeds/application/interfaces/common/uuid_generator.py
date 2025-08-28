from typing import Protocol
from uuid import UUID


class UUIDGenerator(Protocol):
    """Интерфейс для генерации UUID."""

    @staticmethod
    def __call__() -> UUID:
        """Генерирует новый UUID."""
        ...
