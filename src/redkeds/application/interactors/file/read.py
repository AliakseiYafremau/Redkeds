from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.domain.entities.file_id import FileId


class ReadFileInteractor:
    """Интерактор для выдачи файла."""

    def __init__(self, file_manager: FileManager) -> None:
        self._file_manager = file_manager

    async def __call__(self, file_id: FileId) -> bytes:
        """Выдает файл."""
        return await self._file_manager.read(file_id)
