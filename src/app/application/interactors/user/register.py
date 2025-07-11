from typing import Protocol

from app.application.dto.user import NewUserDTO
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.showcase.showcase_gateway import ShowcaseSaver
from app.application.interfaces.user.password_manager import PasswordHasher
from app.application.interfaces.user.user_gateway import UserReader, UserSaver
from app.domain.entities.showcase import Showcase, ShowcaseId
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId
from app.domain.services.password import validate_password


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
        transaction_manager: TransactionManager,
    ) -> None:
        self._user_gateway = user_gateway
        self._showcase_gateway = showcase_gateway
        self._uuid_generator = uuid_generator
        self._password_hasher = password_hasher
        self._transaction_manager = transaction_manager

    async def __call__(self, data: NewUserDTO) -> UserId:
        """Создаёт и сохраняет нового пользователя.

        Args:
            data (NewUserDTO): Данные для регистрации нового пользователя.

        """
        validate_password(data.password)
        user_id = UserId(self._uuid_generator())
        hashed_password = self._password_hasher.hash_password(data.password)
        showcase = Showcase(id=ShowcaseId(self._uuid_generator()), owner_id=user_id)
        await self._showcase_gateway.save_showcase(showcase)
        user = User(
            id=user_id,
            username=data.username,
            password=hashed_password,
            photo=data.photo,
            specialization=data.specialization,
            city=data.city,
            description=data.description,
            tags=data.tags,
            communication_method=data.communication_method,
            status=data.status,
            showcase=None,
        )
        await self._user_gateway.save_user(user)
        await self._transaction_manager.commit()
        return user_id
