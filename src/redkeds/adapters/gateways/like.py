from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import LikeModel
from redkeds.application.interfaces.like.like_gateway import LikeGateway
from redkeds.domain.entities.like import Like, LikeId
from redkeds.domain.entities.showcase import ShowcaseId
from redkeds.domain.entities.user_id import UserId


class SQLLikeGateway(LikeGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_like_by_id(self, like_id: LikeId) -> Like:
        statement = select(LikeModel).where(LikeModel.id == like_id)
        result = await self._session.execute(statement)
        like_model = result.scalar_one_or_none()
        if like_model is None:
            raise ValueError(f"Like with id {like_id} not found")
        return Like(
            id=LikeId(like_model.id),
            user_id=UserId(like_model.user_id),
            showcase_id=ShowcaseId(like_model.showcase_id),
        )

    async def save_like(self, like: Like) -> LikeId | None:
        like_model = LikeModel(
            id=like.id,
            user_id=like.user_id,
            showcase_id=like.showcase_id,
        )
        self._session.add(like_model)
        return like.id

    async def delete_like(self, like_id: LikeId) -> None:
        statement = select(LikeModel).where(LikeModel.id == like_id)
        result = await self._session.execute(statement)
        like_model = result.scalar_one_or_none()
        if like_model is None:
            raise ValueError(f"Like with id {like_id} not found")
        await self._session.delete(like_model)
