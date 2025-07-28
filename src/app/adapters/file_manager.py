from pathlib import Path

from app.application.interfaces.common.file_gateway import FileManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.domain.entities.file_id import FileId


class LocalFileManager(FileManager):
    """Менеджер файлов."""

    def __init__(self, directory: Path, uuid_generator: UUIDGenerator) -> None:
        self._directory = directory
        self._uuid_generator = uuid_generator

        self._directory.mkdir(parents=True, exist_ok=True)

    async def save(self, file: bytes) -> FileId:
        """Сохраняет файл."""
        file_id = FileId(self._uuid_generator())
        file_path = self._directory / str(file_id)

        with file_path.open("wb") as f:
            f.write(file)

        return file_id

    async def read(self, file_id: FileId) -> bytes:
        """Отдает файл."""
        file_path = self._directory / str(file_id)

        if not file_path.exists():
            raise FileNotFoundError(f"File with id {file_id} not found")

        with file_path.open("rb") as f:
            return f.read()

    async def delete(self, file_id: FileId) -> None:
        """Удаляет файл."""
        file_path = self._directory / str(file_id)
        if file_path.exists():
            file_path.unlink()
        else:
            raise FileNotFoundError(f"File with id {file_id} not found")

    async def update(self, file_id: FileId, file: bytes) -> None:
        """Обновляет файл."""
        file_path = self._directory / str(file_id)
        if not file_path.exists():
            raise FileNotFoundError(f"File with id {file_id} not found")
        with file_path.open("wb") as f:
            f.write(file)
