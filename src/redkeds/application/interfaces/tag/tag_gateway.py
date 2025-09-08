from typing import Protocol

from redkeds.domain.entities.tag import Tag


class TagGateway(Protocol):
    async def get_tags(self) -> list[Tag]: ...
