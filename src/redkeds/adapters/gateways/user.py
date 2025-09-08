from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from redkeds.adapters.exceptions import TargetNotFoundError
from redkeds.adapters.mappers import map_model_to_user, map_user_to_model
from redkeds.adapters.models import (
    DefaultPhotoModel,
    UserModel,
    UserSpecializationModel,
    UserTagModel,
)
from redkeds.application.interfaces.user.default_photo_gateway import (
    DefaultPhotoGateway,
)
from redkeds.application.interfaces.user.user_gateway import UserGateway
from redkeds.domain.entities.file_id import FileId
from redkeds.domain.entities.user import User, UserId


class SQLUserGateway(UserGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def save_user(
        self,
        user: User,
    ) -> None:
        user_model = map_user_to_model(user)
        self._session.add(user_model)
        # Сохраняем связи с тегами
        for tag_id in user.tags:
            user_tag = UserTagModel(user_id=user.id, tag_id=tag_id)
            self._session.add(user_tag)
        # Сохраняем связи со специализациями
        for spec_id in user.specialization:
            user_spec = UserSpecializationModel(
                user_id=user.id, specialization_id=spec_id
            )
            self._session.add(user_spec)

    async def get_user_by_id(self, user_id: UserId) -> User:
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
        user_model.default_photo = user.default_photo

        # Удаляем старые связи с тегами
        await self._session.execute(
            delete(UserTagModel).where(UserTagModel.user_id == user.id)
        )
        # Добавляем новые связи с тегами
        for tag_id in user.tags:
            user_tag = UserTagModel(user_id=user.id, tag_id=tag_id)
            self._session.add(user_tag)

        # Удаляем старые связи со специализациями
        await self._session.execute(
            delete(UserSpecializationModel).where(
                UserSpecializationModel.user_id == user.id
            )
        )
        # Добавляем новые связи со специализациями
        for spec_id in user.specialization:
            user_spec = UserSpecializationModel(
                user_id=user.id, specialization_id=spec_id
            )
            self._session.add(user_spec)

    async def delete_user(self, user_id: UserId) -> None:
        statement = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(statement)
        user_model = result.scalar_one_or_none()

        if user_model is None:
            raise TargetNotFoundError(f"User with id {user_id} not found")

        # Удаляем все связи с тегами
        await self._session.execute(
            delete(UserTagModel).where(UserTagModel.user_id == user_id)
        )
        # Удаляем все связи со специализациями
        await self._session.execute(
            delete(UserSpecializationModel).where(
                UserSpecializationModel.user_id == user_id
            )
        )
        await self._session.delete(user_model)


class SQLDefaultPhotoGateway(DefaultPhotoGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_default_photos(self) -> list[FileId]:
        statement = select(DefaultPhotoModel)
        result = await self._session.execute(statement)
        default_photos = result.scalars().all()

        return [FileId(photo.id) for photo in default_photos]
