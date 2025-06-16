from app.application.dto.user import UserDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.user.user_gateway import UserReader


class ReadUserInteractor:
    """Интерактор для получения информации о пользователе."""

    def __init__(
        self,
        user_gateway: UserReader,
        id_provider: IdProvider,
    ) -> None:
        self._user_gateway = user_gateway
        self._id_provider = id_provider

    def __call__(self) -> UserDTO:
        """Возвращает данные пользователя."""
        user_id = self._id_provider()
        user = self._user_gateway.get_user_by_id(user_id)
        return UserDTO(
            username=user.username,
            photo=user.photo,
            specialization=user.specialization,
            city=user.city,
            description=user.description,
            communication_method=user.communication_method,
            status=user.status,
            showcase=user.showcase,
        )
