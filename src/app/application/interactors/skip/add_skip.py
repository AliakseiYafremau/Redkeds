from app.application.dto.skip import NewSkipDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.skip.skip_gateway import SkipSaver
from app.domain.entities.skip import Skip, SkipId


class AddSkipInteractor:
    """Интерактор для добавления скипов."""

    def __init__(
        self,
        id_provider: IdProvider,
        skip_gateway: SkipSaver,
        transaction_manager: TransactionManager,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._id_provider = id_provider
        self._skip_gateway = skip_gateway
        self._transaction_manager = transaction_manager
        self._uuid_generator = uuid_generator

    async def __call__(self, data: NewSkipDTO) -> SkipId:
        """Добавляет скип."""
        user_id = self._id_provider()
        skip_id = SkipId(self._uuid_generator())
        skip = Skip(
            id=skip_id,
            user_id=user_id,
            showcase_id=data.showcase_id,
        )
        await self._skip_gateway.add_skip(skip)
        await self._transaction_manager.commit()
        return skip_id
