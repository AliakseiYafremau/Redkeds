from typing import Protocol

from redkeds.application.dto.user import NewUserDTO
from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.common.uuid_generator import UUIDGenerator
from redkeds.application.interfaces.showcase.showcase_gateway import ShowcaseSaver
from redkeds.application.interfaces.user.default_photo_gateway import DefaultPhotoReader
from redkeds.application.interfaces.user.password_manager import PasswordHasher
from redkeds.application.interfaces.user.user_gateway import UserReader, UserSaver
from redkeds.domain.entities.showcase import Showcase, ShowcaseId
from redkeds.domain.entities.user import User
from redkeds.domain.entities.user_id import UserId
from redkeds.domain.services.password import validate_password


class UserGateway(UserSaver, UserReader, Protocol):
    """Интерфейс сохранения и чтения пользователя."""


class RegisterUserInteractor:
    """Интерактор для регистрации нового пользователя."""

    def __init__(
        self,
        user_gateway: UserGateway,
        showcase_gateway: ShowcaseSaver,
        uuid_generator: UUIDGenerator,
        password_hasher: PasswordHasher,
        file_manager: FileManager,
        default_photo_reader: DefaultPhotoReader,
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_gateway = user_gateway
        self._showcase_gateway = showcase_gateway
        self._default_photo_reader = default_photo_reader
        self._uuid_generator = uuid_generator
        self._password_hasher = password_hasher
        self._file_manager = file_manager
        self._transaction_manager = transaction_manager

    async def __call__(self, data: NewUserDTO) -> UserId:
        """Создаёт и сохраняет нового пользователя.

        Args:
            data (NewUserDTO): Данные для регистрации нового пользователя.

        """
        validate_password(data.password)

        if data.default_photo is not None and data.photo is not None:
            raise ValueError("Нельзя указать и фото, и фото по умолчанию одновременно.")
        user_id = UserId(self._uuid_generator())
        hashed_password = self._password_hasher.hash_password(data.password)
        showcase = Showcase(id=ShowcaseId(self._uuid_generator()))
        await self._showcase_gateway.save_showcase(showcase)

        if data.default_photo is not None:
            default_photos = await self._default_photo_reader.get_default_photos()
            if data.default_photo not in default_photos:
                raise ValueError("Указанное фото по умолчанию не найдено.")

        photo_id = None
        if data.photo is not None:
            photo_id = await self._file_manager.save(data.photo)

        user = User(
            id=user_id,
            email=data.email,
            username=data.username,
            nickname=data.nickname,
            password=hashed_password,
            photo=photo_id,
            default_photo=data.default_photo,
            specialization=data.specialization,
            city=data.city,
            description=data.description,
            tags=data.tags,
            communication_method=data.communication_method,
            status=data.status,
            showcase=showcase.id,
            name_display=data.name_display,
        )
        await self._user_gateway.save_user(user)
        await self._transaction_manager.commit()
        return user_id
