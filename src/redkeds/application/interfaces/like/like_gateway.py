from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.like import Like, LikeId


class LikeGateway(Protocol):
    @abstractmethod
    async def add_like(self, like: Like) -> LikeId:
        raise NotImplementedError

    @abstractmethod
    async def delete_like(self, like_id: LikeId) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_like_by_id(self, like_id: LikeId) -> Like:
        raise NotImplementedError
