from typing import Protocol

from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
)
from app.application.interfaces.user.user_gateway import UserDeleter


class ShowcaseGateway(ShowcaseReader, ShowcaseDeleter, Protocol):
    """Интерфейс чтения и удаления витрины."""


class DeleteUserInteractor:
    """Интерактор для удаления пользователя."""

    def __init__(
        self,
        user_gateway: UserDeleter,
        showcase_gateway: ShowcaseGateway,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_gateway = user_gateway
        self._showcase_gateway = showcase_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self) -> None:
        """Удаляет пользователя."""
        user_id = self._id_provider()
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        await self._user_gateway.delete_user(user_id)
        await self._showcase_gateway.delete_showcase(showcase.id)
        await self._transaction_manager.commit()
