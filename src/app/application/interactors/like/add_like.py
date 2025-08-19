from app.application.dto.like import NewLikeDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.like.like_gateway import LikeSaver
from app.domain.entities.like import Like, LikeId


class AddLikeInteractor:
    """Интерактор для добавления лайков."""

    def __init__(
        self,
        id_provider: IdProvider,
        like_gateway: LikeSaver,
        transaction_manager: TransactionManager,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._id_provider = id_provider
        self._like_gateway = like_gateway
        self._transaction_manager = transaction_manager
        self._uuid_generator = uuid_generator

    async def __call__(self, data: NewLikeDTO) -> LikeId:
        """Добавляет лайк."""
        user_id = self._id_provider()
        like_id = LikeId(self._uuid_generator())
        like = Like(
            id=like_id,
            user_id=user_id,
            showcase_id=data.showcase_id,
        )
        await self._like_gateway.add_like(like)
        await self._transaction_manager.commit()
        return like_id
