from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.skip import Skip, SkipId


class SkipGateway(Protocol):
    @abstractmethod
    async def save_skip(self, skip: Skip) -> SkipId:
        raise NotImplementedError

    @abstractmethod
    async def delete_skip(self, skip_id: SkipId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_skip_by_id(self, skip_id: SkipId) -> Skip:
        raise NotImplementedError
