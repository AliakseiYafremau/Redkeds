from app.application.dto.user import UpdateUserDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.user.user_gateway import UserReader, UserUpdater
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


class UpdateUserInteractor:
    """Интерактор для обновления пользователя."""

    def __init__(
        self,
        user_reader_gateway: UserReader,
        user_updater_gateway: UserUpdater,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_reader_gateway = user_reader_gateway
        self._user_updater_gateway = user_updater_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    def __call__(self, data: UpdateUserDTO) -> UserId:
        """Обновляет данные пользователя."""
        user_id = self._id_provider()
        user = self._user_reader_gateway.get_user_by_id(user_id)
        self.update_user(user, data)
        self._user_updater_gateway.update_user(user)
        self._transaction_manager.commit()

        return user.id

    def update_user(
        self,
        user: User,
        new_data: UpdateUserDTO,
    ) -> None:
        """Обновляет сущность пользователя."""
        if new_data.username is not None:
            user.username = new_data.username
        if new_data.photo is not None:
            user.photo = new_data.photo
        if new_data.specialization is not None:
            user.specialization = new_data.specialization
        if new_data.city is not None:
            user.city = new_data.city
        if new_data.description is not None:
            user.description = new_data.description
        if new_data.tags is not None:
            user.tags = new_data.tags
        if new_data.communication_method is not None:
            user.connection_method = new_data.communication_method
        if new_data.status is not None:
            user.status = new_data.status
        if new_data.showcase is not None:
            user.showcase = new_data.showcase
