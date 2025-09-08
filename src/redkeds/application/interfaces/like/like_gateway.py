from typing import Protocol

from redkeds.domain.entities.like import Like, LikeId


class LikeGateway(Protocol):
    async def add_like(self, like: Like) -> LikeId: ...

    async def delete_like(self, like_id: LikeId) -> None: ...

    async def get_like_by_id(self, like_id: LikeId) -> Like: ...
