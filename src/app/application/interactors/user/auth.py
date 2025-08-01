from app.application.dto.user import LoginUserDTO
from app.application.interfaces.user.password_manager import PasswordHasher
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.user_id import UserId


class AuthUserInteractor:
    """Интерактор для аутентификации пользователя."""

    def __init__(
        self,
        user_gateway: UserReader,
        password_hasher: PasswordHasher,
    ) -> None:
        self._user_gateway = user_gateway
        self._password_hasher = password_hasher

    async def __call__(self, data: LoginUserDTO) -> UserId:
        """Атуентификация пользователя.

        Args:
            data (LoginUserDTO): Данные для аутентификации пользователя.

        """
        user = await self._user_gateway.get_user_by_email(data.email)
        self._password_hasher.verify_password(
            data.password,
            user.password,
        )
        return user.id
