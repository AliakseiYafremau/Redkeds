from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import SkipModel
from redkeds.application.interfaces.skip.skip_gateway import SkipGateway
from redkeds.domain.entities.showcase import ShowcaseId
from redkeds.domain.entities.skip import Skip, SkipId
from redkeds.domain.entities.user_id import UserId


class SQLSkipGateway(SkipGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_skip_by_id(self, skip_id: SkipId) -> Skip:
        statement = select(SkipModel).where(SkipModel.id == skip_id)
        result = await self._session.execute(statement)
        skip_model = result.scalar_one_or_none()
        if skip_model is None:
            raise ValueError(f"Skip with id {skip_id} not found")
        return Skip(
            id=SkipId(skip_model.id),
            user_id=UserId(skip_model.user_id),
            showcase_id=ShowcaseId(skip_model.showcase_id),
        )

    async def save_skip(self, skip: Skip) -> SkipId:
        skip_model = SkipModel(
            id=skip.id,
            user_id=skip.user_id,
            showcase_id=skip.showcase_id,
        )
        self._session.add(skip_model)
        return skip.id

    async def delete_skip(self, skip_id: SkipId) -> None:
        statement = select(SkipModel).where(SkipModel.id == skip_id)
        result = await self._session.execute(statement)
        skip_model = result.scalar_one_or_none()
        if skip_model is None:
            raise ValueError(f"Skip with id {skip_id} not found")
        await self._session.delete(skip_model)
