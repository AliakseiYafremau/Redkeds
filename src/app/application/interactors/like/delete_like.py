from typing import Protocol

from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.like.like_gateway import LikeDeleter, LikeReader
from app.domain.entities.like import LikeId
from app.domain.services.like_service import ensure_can_manage_like


class LikeGateway(LikeDeleter, LikeReader, Protocol):
    """Интерфейс для удаления лайка."""


class DeleteLikeInteractor:
    """Интерактор для удаления лайков."""

    def __init__(
        self,
        like_gateway: LikeGateway,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._like_gateway = like_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self, like_id: LikeId) -> None:
        """Удаляет лайк."""
        user_id = self._id_provider()
        like = await self._like_gateway.get_like_by_id(like_id)
        await self._like_gateway.delete_like(like_id)
        ensure_can_manage_like(like, user_id)
        await self._transaction_manager.commit()
