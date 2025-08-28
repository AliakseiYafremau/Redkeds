from typing import Protocol

from redkeds.domain.entities.file_id import FileId


class DefaultPhotoReader(Protocol):
    """Интерфейс для чтения доступных фото по умолчанию."""

    async def get_default_photos(self) -> list[FileId]:
        """Получает URL фото по умолчанию."""
        ...
