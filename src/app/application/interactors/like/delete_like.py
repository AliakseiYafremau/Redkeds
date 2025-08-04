
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.like.like_geteway import DeleteLike, IdProvider


class DeleteLikeInteractor:
    """Интерактор для удаления лайков."""

    def __init__(
        self,
        user_gateway: UserDeleter,
        like_gateway: DeleteLike,
        # transaction_manager: TransactionManager,

        # showcase_gateway: ShowcaseGateway,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._like_gateway = like_gateway
        # self._showcase_gateway = showcase_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self) -> None:
        """Удаляет лайк."""
        like_id = self._id_provider()
        # showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        await self._like_gateway.delete_like(like_id)
        # await self._showcase_gateway.delete_showcase(showcase.id)
        await self._transaction_manager.commit()
