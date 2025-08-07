from typing import Protocol

from app.application.interfaces.common.file_gateway import FileManager
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
)
from app.application.interfaces.user.user_gateway import UserDeleter, UserReader


class ShowcaseGateway(ShowcaseReader, ShowcaseDeleter, Protocol):
    """Интерфейс чтения и удаления витрины."""


class UserGateway(UserDeleter, UserReader, Protocol):
    """Интерфейс чтения и удаления витрины."""


class DeleteUserInteractor:
    """Интерактор для удаления пользователя."""

    def __init__(
        self,
        user_gateway: UserGateway,
        showcase_gateway: ShowcaseGateway,
        id_provider: IdProvider,
        file_manager: FileManager,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_gateway = user_gateway
        self._showcase_gateway = showcase_gateway
        self._id_provider = id_provider
        self._file_manager = file_manager
        self._transaction_manager = transaction_manager

    async def __call__(self) -> None:
        """Удаляет пользователя."""
        user_id = self._id_provider()
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        user = await self._user_gateway.get_user_by_id(user_id)
        await self._showcase_gateway.delete_showcase(showcase.id)
        await self._user_gateway.delete_user(user_id)
        if user.photo is not None:
            await self._file_manager.delete(user.photo)
        await self._transaction_manager.commit()
