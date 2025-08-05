from app.application.dto.like import NewLikeDTO
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.like.like_geteway import LikeSaver
from app.domain.entities.like import Like, LikeId


class AddLikeInteractor:
    """Интерактор для добавления лайков."""

    def __init__(
        self,
        like_gateway: LikeSaver,
        transaction_manager: TransactionManager,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._like_gateway = like_gateway
        self._transaction_manager = transaction_manager
        self._uuid_generator = uuid_generator

    async def __call__(self, data: NewLikeDTO) -> LikeId:
        """Добавляет лайк."""
        like_id = LikeId(self._uuid_generator())
        like = Like(
            id=like_id,
            user_id=data.user_id,
            showcase_id=data.showcase_id,
        )
        await self._like_gateway.add_like(like)
        await self._transaction_manager.commit()
        return like_id
