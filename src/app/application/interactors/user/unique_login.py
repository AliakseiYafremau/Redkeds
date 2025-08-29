
from app.application.interfaces.user.user_gateway import UserReader


class UniqueLoginInteractor:
    """Интерактор для проверки уникальности логина."""

    def __init__(self, user_gateway: UserReader) -> None:
        self._user_gateway = user_gateway

    async def __call__(self, email: str) -> bool:
        """Получение пользователя по email."""
        return bool(await self._user_gateway.get_user_by_email(email))
