from uuid import uuid4

from app.application.interfaces.user.user_gateway import (
    UserDeleter,
    UserReader,
    UserSaver,
    UserUpdater,
)
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.user import User, UserId


class UserGateway(
    UserSaver,
    UserUpdater,
    UserReader,
    UserDeleter,
):
    """Gateway для работы с данными пользователя."""

    async def save_user(
        self,
        user: User,
    ) -> None:
        """Сохраняет пользователя в базе данных."""

    async def get_user_by_id(self, user_id: UserId) -> User:
        """Получает пользователя по id."""
        return User(
            id=user_id,
            username="fake_username",
            password="fake_password",
            photo=None,
            specialization=[],
            city=CityId(uuid4()),
            description="fake_description",
            tags=[],
            communication_method=CommunicationMethodId(uuid4()),
            status=None,
            showcase=None,
        )

    async def get_user_by_username(self, username: str) -> User:
        """Получает пользователя по имени."""
        return User(
            id=UserId(uuid4()),
            username=username,
            password="fake_password",
            photo=None,
            specialization=[],
            city=CityId(uuid4()),
            description="fake_description",
            tags=[],
            communication_method=CommunicationMethodId(uuid4()),
            status=None,
            showcase=None,
        )

    async def update_user(self, user: User) -> None:
        """Обновляет данные пользователя."""

    async def delete_user(self, user: UserId) -> None:
        """Удаляет пользователя."""
