from typing import Protocol

from app.domain.entities.file_id import FileId


class FileManager(Protocol):
    """Интерфейс для управления файлами."""

    async def save(self, file: bytes) -> FileId:
        """Сохраняет файл."""
        ...

    async def read(self, file_id: FileId) -> bytes:
        """Отдает файл."""
        ...

    async def update(self, file_id: FileId, file: bytes) -> None:
        """Обновляет файл."""

    async def delete(self, file_id: FileId) -> None:
        """Удаляет файл."""
        ...
