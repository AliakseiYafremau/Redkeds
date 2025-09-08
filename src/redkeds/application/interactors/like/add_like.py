from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.common.uuid_generator import UUIDGenerator
from redkeds.application.interfaces.like.like_gateway import LikeGateway
from redkeds.domain.entities.like import Like, LikeId
from redkeds.domain.entities.showcase import ShowcaseId


class AddLikeInteractor:
    """Интерактор для добавления лайков."""

    def __init__(
        self,
        id_provider: IdProvider,
        like_gateway: LikeGateway,
        transaction_manager: TransactionManager,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._id_provider = id_provider
        self._like_gateway = like_gateway
        self._transaction_manager = transaction_manager
        self._uuid_generator = uuid_generator

    async def __call__(self, showcase_id: ShowcaseId) -> LikeId:
        """Добавляет лайк."""
        user_id = self._id_provider()
        like_id = LikeId(self._uuid_generator())
        like = Like(
            id=like_id,
            user_id=user_id,
            showcase_id=showcase_id,
        )
        await self._like_gateway.add_like(like)
        await self._transaction_manager.commit()
        return like_id
