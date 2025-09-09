from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.tag import Tag


class TagGateway(Protocol):
    @abstractmethod
    async def get_tags(self) -> list[Tag]:
        raise NotImplementedError
