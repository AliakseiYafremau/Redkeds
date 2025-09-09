from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.file_id import FileId


class DefaultPhotoGateway(Protocol):
    @abstractmethod
    async def get_default_photos(self) -> list[FileId]:
        """Return all default photos."""
        raise NotImplementedError
