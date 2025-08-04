from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.like.like_geteway import IdProvider, LikeDeleter


class DeleteLikeInteractor:
    """Интерактор для удаления лайков."""

    def __init__(
        self,
        like_gateway: LikeDeleter,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._like_gateway = like_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self) -> None:
        """Удаляет лайк."""
        like_id = self._id_provider()
        await self._like_gateway.delete_like(like_id)
        await self._transaction_manager.commit()
