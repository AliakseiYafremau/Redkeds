from typing import Protocol

from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.skip.skip_gateway import SkipDeleter, SkipReader
from redkeds.domain.entities.skip import SkipId
from redkeds.domain.services.skip_service import ensure_can_manage_skip
from redkeds.main.logs import get_logger

logger = get_logger(__name__)


class SkipGateway(SkipDeleter, SkipReader, Protocol):
    """Интерфейс для удаления скипа."""


class DeleteSkipInteractor:
    """Интерактор для удаления скипов."""

    def __init__(
        self,
        skip_gateway: SkipGateway,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._skip_gateway = skip_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self, skip_id: SkipId) -> None:
        """Удаляет лайк."""
        user_id = self._id_provider()
        skip = await self._skip_gateway.get_skip_by_id(skip_id)
        logger.info(skip.user_id)
        logger.info(user_id)
        ensure_can_manage_skip(skip, user_id)
        await self._skip_gateway.delete_skip(skip_id)
        await self._transaction_manager.commit()
