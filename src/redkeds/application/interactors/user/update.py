from typing import Protocol

from redkeds.application.dto.user import UpdateUserDTO
from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.user.user_gateway import UserReader, UserUpdater
from redkeds.domain.entities.user import User


class UserGateway(UserReader, UserUpdater, Protocol):
    """Протокол, включающий в себя интерфейсы обновления и чтения пользователя."""


class UpdateUserInteractor:
    """Интерактор для обновления пользователя."""

    def __init__(
        self,
        user_gateway: UserGateway,
        id_provider: IdProvider,
        file_manager: FileManager,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_gateway = user_gateway
        self._id_provider = id_provider
        self._file_manager = file_manager
        self._transaction_manager = transaction_manager

    async def __call__(self, data: UpdateUserDTO) -> None:
        """Обновляет данные пользователя.

        Args:
            data (UpdateUserDTO): Данные для обновления пользователя.

        """
        user_id = self._id_provider()
        user = await self._user_gateway.get_user_by_id(user_id)
        self.update_user(user, data)

        if data.photo is not None:
            if user.photo is not None:
                await self._file_manager.update(user.photo, data.photo)
            else:
                file_id = await self._file_manager.save(data.photo)
                user.photo = file_id

        await self._user_gateway.update_user(user)
        await self._transaction_manager.commit()

    def update_user(  # noqa: C901
        self,
        user: User,
        new_data: UpdateUserDTO,
    ) -> None:
        """Обновляет сущность пользователя."""
        if new_data.email is not None:
            user.email = new_data.email
        if new_data.username is not None:
            user.username = new_data.username
        if new_data.nickname is not None:
            user.nickname = new_data.nickname
        if new_data.specialization is not None:
            user.specialization = new_data.specialization
        if new_data.city is not None:
            user.city = new_data.city
        if new_data.description is not None:
            user.description = new_data.description
        if new_data.tags is not None:
            user.tags = new_data.tags
        if new_data.communication_method is not None:
            user.communication_method = new_data.communication_method
        if new_data.status is not None:
            user.status = new_data.status
        if new_data.showcase is not None:
            user.showcase = new_data.showcase
        if new_data.name_display is not None:
            user.name_display = new_data.name_display
