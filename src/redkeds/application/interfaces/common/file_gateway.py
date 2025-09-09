from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.file_id import FileId


class FileManager(Protocol):
    @abstractmethod
    async def save(self, file: bytes) -> FileId:
        raise NotImplementedError

    @abstractmethod
    async def read(self, file_id: FileId) -> bytes:
        raise NotImplementedError

    @abstractmethod
    async def update(self, file_id: FileId, file: bytes) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, file_id: FileId) -> None:
        raise NotImplementedError
