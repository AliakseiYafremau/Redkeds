from typing import Protocol
from uuid import UUID

from app.domain.entities.file_id import FileId


class FileManager(Protocol):
    """Интерфейс для управления файлами."""

    async def save(self, file: bytes) -> UUID:
        """Сохраняет файл."""
        ...

    async def read(self, file_id: FileId) -> bytes:
        """Отдает файл."""
        ...

    async def delete(self, file_id: FileId) -> None:
        """Удаляет файл."""
        ...
