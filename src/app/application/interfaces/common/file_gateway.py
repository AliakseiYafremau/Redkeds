from typing import Protocol
from uuid import UUID


class FileManager(Protocol):
    """Интерфейс для управления файлами."""

    async def save(self) -> UUID:
        """Сохраняет файл."""
        ...
