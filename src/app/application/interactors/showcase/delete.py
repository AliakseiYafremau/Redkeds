from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.showcase.showcase_gateway import ShowcaseDeleter, ShowcaseReader
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.showcase import ShowcaseId
from typing import Protocol


class ShowcaseGateway(ShowcaseDeleter, ShowcaseReader, Protocol):
    """Протокол, включающий в себя чтение и удаление."""


class DeleteShowcaseInteractor:
    """Интерактор для удаления витрины."""

    def __init__(
        self,
        id_provider: IdProvider,
        showcase_gateway: ShowcaseGateway,
        user_gateway: UserReader,
        transaction_manager: TransactionManager,
    ) -> None:
        self._id_provider = id_provider
        self._showcase_gateway = showcase_gateway
        self._user_gateway = user_gateway
        self._transactoin_manager = transaction_manager

    async def __call__(self) -> None:
        """Удаляет витрину."""
        user_id = self._id_provider()
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        await self._showcase_gateway.delete_showcase(showcase.id)
        await self._transactoin_manager.commit()
