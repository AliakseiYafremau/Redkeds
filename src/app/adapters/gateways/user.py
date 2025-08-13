from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.exceptions import TargetNotFoundError
from app.adapters.mappers import map_model_to_user, map_user_to_model
from app.adapters.models import UserModel
from app.application.interfaces.user.user_gateway import (
    UserDeleter,
    UserReader,
    UserSaver,
    UserUpdater,
)
from app.domain.entities.user import User, UserId


class UserGateway(
    UserSaver,
    UserUpdater,
    UserReader,
    UserDeleter,
):
    """Gateway для работы с данными пользователя."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save_user(
        self,
        user: User,
    ) -> None:
        """Сохраняет пользователя в базе данных."""
        user_model = map_user_to_model(user)
        self._session.add(user_model)

    async def get_user_by_id(self, user_id: UserId) -> User:
        """Получает пользователя по id."""
        statement = (
            select(UserModel)
            .where(UserModel.id == user_id)
            .options(
                selectinload(UserModel.specializations), selectinload(UserModel.tags)
            )
        )
        result = await self._session.execute(statement)
        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise TargetNotFoundError(f"User with id {user_id} not found")

        return map_model_to_user(user_model)

    async def get_user_by_email(self, email: str) -> User:
        """Получает пользователя по имени."""
        statement = (
            select(UserModel)
            .where(UserModel.email == email)
            .options(
                selectinload(UserModel.specializations), selectinload(UserModel.tags)
            )
        )
        result = await self._session.execute(statement)
        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise TargetNotFoundError(f"User with email {email} not found")

        return map_model_to_user(user_model)

    async def update_user(self, user: User) -> None:
        """Обновляет данные пользователя."""
        statement = select(UserModel).where(UserModel.id == user.id)
        result = await self._session.execute(statement)
        user_model = result.scalar_one()

        if user_model is None:
            raise TargetNotFoundError(f"User with id {user.id} not found")

        user_model.username = user.username
        user_model.password = user.password
        user_model.photo = user.photo
        user_model.description = user.description
        user_model.status = user.status
        user_model.city_id = user.city
        user_model.communication_method_id = user.communication_method
        user_model.showcase_id = user.showcase
        user_model.name_display = user.name_display

    async def delete_user(self, user_id: UserId) -> None:
        """Удаляет пользователя."""
        statement = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(statement)
        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise TargetNotFoundError(f"User with id {user_id} not found")

        await self._session.delete(user_model)
