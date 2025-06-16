from typing import Protocol
from uuid import UUID


class UUIDGenerator(Protocol):
    """Интерфейс для генерации UUID."""

    def __call__(self) -> UUID:
        """Генерирует новый UUID."""
        ...
