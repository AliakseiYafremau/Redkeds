from collections.abc import AsyncIterable
from uuid import uuid4

from dishka import Provider, Scope, provide
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from redkeds.adapters.database import new_async_engine, new_session_maker
from redkeds.adapters.file_manager import LocalFileManager
from redkeds.adapters.gateways.chat import SQLChatGateway, SQLChatMessageGateway
from redkeds.adapters.gateways.city import SQLCityGateway
from redkeds.adapters.gateways.communication_method import SQLCommunicationMethodGateway
from redkeds.adapters.gateways.like import SQLLikeGateway
from redkeds.adapters.gateways.showcase import SQLShowcaseGateway, SQLWorkGateway
from redkeds.adapters.gateways.skip import SQLSkipGateway
from redkeds.adapters.gateways.specialization import SQLSpecializationGateway
from redkeds.adapters.gateways.tag import SQLTagGateway
from redkeds.adapters.gateways.user import SQLDefaultPhotoGateway, SQLUserGateway
from redkeds.adapters.id_provider import JWTTokenManager, TokenIdProvider
from redkeds.adapters.password import BcryptPasswordHasher
from redkeds.adapters.transaction import SQLTransactionManager
from redkeds.application.interfaces.chat.chat_gateway import ChatGateway
from redkeds.application.interfaces.chat.chat_message_gateway import ChatMessageGateway
from redkeds.application.interfaces.city.city_gateway import CityGateway
from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.common.uuid_generator import UUIDGenerator
from redkeds.application.interfaces.communication_method.communication_method_gateway import (  # noqa: E501
    CommunicationMethodGateway,
)
from redkeds.application.interfaces.like.like_gateway import LikeGateway
from redkeds.application.interfaces.showcase.showcase_gateway import ShowcaseGateway
from redkeds.application.interfaces.showcase.work_gateway import WorkGateway
from redkeds.application.interfaces.skip.skip_gateway import SkipGateway
from redkeds.application.interfaces.specialization.specialization_gateway import (
    SpecializationGateway,
)
from redkeds.application.interfaces.tag.tag_gateway import TagGateway
from redkeds.application.interfaces.user.default_photo_gateway import (
    DefaultPhotoGateway,
)
from redkeds.application.interfaces.user.password_manager import PasswordHasher
from redkeds.application.interfaces.user.user_gateway import UserGateway
from redkeds.main.config import (
    MediaConfig,
    PostgresConfig,
    TokenConfig,
)


class InterfacesProvider(Provider):
    """Провайдер приложения.

    Организуем и управляет фабриками для создания зависимостей.
    """

    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        """Возвращает генератор UUID."""
        return uuid4

    @provide(scope=Scope.APP)
    def get_session_maker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        """Возвращает фабрику сессий для работы с базой данных."""
        return new_session_maker(engine=engine)

    @provide(scope=Scope.APP)
    def get_engine(
        self,
        config: PostgresConfig,
    ) -> AsyncEngine:
        """Возвращает новый двигатель для работы с базой данных."""
        return new_async_engine(
            login=config.login,
            password=config.password,
            host=config.host,
            port=config.port,
            database=config.name,
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        """Возвращает сессию для работы с базой данных."""
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def get_jwt_manager(self, config: TokenConfig) -> JWTTokenManager:
        """Возвращает менеджер jwt-токенов."""
        return JWTTokenManager(config)

    @provide(scope=Scope.REQUEST)
    def get_id_provider(self, manager: JWTTokenManager, request: Request) -> IdProvider:
        """Возвращает провайдер идентификаторов."""
        return TokenIdProvider(manager, request)

    @provide(scope=Scope.REQUEST)
    def get_file_manager(
        self, config: MediaConfig, uuid_generator: UUIDGenerator
    ) -> FileManager:
        """Возвращает менеджер файлов."""
        return LocalFileManager(
            directory=config.media_directory, uuid_generator=uuid_generator
        )

    user_gateway = provide(
        SQLUserGateway,
        scope=Scope.REQUEST,
        provides=UserGateway,
    )
    tag_gateway = provide(
        SQLTagGateway,
        scope=Scope.REQUEST,
        provides=TagGateway,
    )
    communication_method_gateway = provide(
        SQLCommunicationMethodGateway,
        scope=Scope.REQUEST,
        provides=CommunicationMethodGateway,
    )
    specialization_gateway = provide(
        SQLSpecializationGateway,
        scope=Scope.REQUEST,
        provides=SpecializationGateway,
    )
    city_gateway = provide(
        SQLCityGateway,
        scope=Scope.REQUEST,
        provides=CityGateway,
    )
    like_gateway = provide(
        SQLLikeGateway,
        scope=Scope.REQUEST,
        provides=LikeGateway,
    )
    skip_gateway = provide(
        SQLSkipGateway,
        scope=Scope.REQUEST,
        provides=SkipGateway,
    )
    showcase_gateway = provide(
        SQLShowcaseGateway,
        scope=Scope.REQUEST,
        provides=ShowcaseGateway,
    )
    work_gateway = provide(
        SQLWorkGateway,
        scope=Scope.REQUEST,
        provides=WorkGateway,
    )
    chat_gateway = provide(SQLChatGateway, scope=Scope.REQUEST, provides=ChatGateway)
    chat_message_gateway = provide(
        SQLChatMessageGateway, scope=Scope.REQUEST, provides=ChatMessageGateway
    )
    transaction_manager = provide(
        SQLTransactionManager,
        scope=Scope.REQUEST,
        provides=TransactionManager,
    )
    password_hasher = provide(
        BcryptPasswordHasher,
        scope=Scope.REQUEST,
        provides=PasswordHasher,
    )
    default_photo_provider = provide(
        SQLDefaultPhotoGateway,
        scope=Scope.REQUEST,
        provides=DefaultPhotoGateway,
    )
