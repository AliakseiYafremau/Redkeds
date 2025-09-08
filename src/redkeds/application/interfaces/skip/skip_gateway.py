from typing import Protocol

from redkeds.domain.entities.skip import Skip, SkipId


class SkipGateway(Protocol):
    async def save_skip(self, skip: Skip) -> SkipId: ...

    async def delete_skip(self, skip_id: SkipId) -> None: ...

    async def get_skip_by_id(self, skip_id: SkipId) -> Skip: ...
