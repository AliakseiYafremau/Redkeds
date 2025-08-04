from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import LikeModel
from app.application.interfaces.like.like_geteway import LikeDeleter, LikeSaver
from app.domain.entities.like import Like, LikeId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.user_id import UserId


class LikeGateway(LikeSaver, LikeDeleter):
    """Gateway для работы с лайками."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_like_by_id(self, like_id: LikeId) -> Like:
        """Получает лайк по id."""
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
