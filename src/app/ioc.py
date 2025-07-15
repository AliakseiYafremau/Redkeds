from collections.abc import AsyncIterable
from uuid import uuid4

from dishka import AnyOf, Provider, Scope, provide
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.adapters.database import new_session_maker
from app.adapters.gateways.city import CityGateway
from app.adapters.gateways.showcase import ShowcaseGateway
from app.adapters.gateways.specialization import SpecializationGateway
from app.adapters.gateways.tag import TagGateway
from app.adapters.gateways.user import UserGateway
from app.adapters.id_provider import JWTTokenManager, TokenIdProvider
from app.adapters.password import FakePasswordHasher
from app.adapters.transaction import SQLTransactionManager
from app.application.interactors.city.read import ReadCitiesInteractor
from app.application.interactors.specialization.read import (
    ReadSpecializationsInteractor,
)
from app.application.interactors.tag.read import ReadTagsInteractor
from app.application.interactors.user.auth import AuthUserInteractor
from app.application.interactors.user.delete import DeleteUserInteractor
from app.application.interactors.user.delete import (
    ShowcaseGateway as ShowcaseGatewayWithReaderAndDeleter,
)
from app.application.interactors.user.read import ReadUserInteractor
from app.application.interactors.user.register import RegisterUserInteractor
from app.application.interactors.user.register import (
    UserGateway as UserGatewayWithReaderAndSaver,
)
from app.application.interactors.user.update import UpdateUserInteractor
from app.application.interactors.user.update import (
    UserGateway as UserGatewayWithReaderAndDeleter,
)
from app.application.interfaces.city.city_gateway import CityReader
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
    ShowcaseSaver,
)
from app.application.interfaces.specialization.specialization_gateway import (
    SpecializationReader,
)
from app.application.interfaces.tag.tag_gateway import TagReader
from app.application.interfaces.user.password_manager import PasswordHasher
from app.application.interfaces.user.user_gateway import (
    UserDeleter,
    UserReader,
    UserSaver,
    UserUpdater,
)
from app.config import (
    PostgresConfig,
    TokenConfig,
    load_postgres_config,
    load_token_config,
)


class AppProvider(Provider):
    """Провайдер приложения.

    Организуем и управляет фабриками для создания зависимостей.
    """

    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> UUIDGenerator:
        """Возвращает генератор UUID."""
        return uuid4

    @provide(scope=Scope.APP)
    def get_session_maker(
        self, config: PostgresConfig
    ) -> async_sessionmaker[AsyncSession]:
        """Возвращает фабрику сессий для работы с базой данных."""
        return new_session_maker(
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

    @provide(scope=Scope.APP)
    def get_postgres_config(self) -> PostgresConfig:
        """Возвращает конфигурацию подключения к PostgreSQL."""
        return load_postgres_config()

    @provide(scope=Scope.APP)
    def get_token_config(self) -> TokenConfig:
        """Возвращает конфигурацию для токенов."""
        return load_token_config()

    @provide(scope=Scope.REQUEST)
    def get_jwt_manager(self, config: TokenConfig) -> JWTTokenManager:
        """Возвращает менеджер jwt-токенов."""
        return JWTTokenManager(config)

    @provide(scope=Scope.REQUEST)
    def get_id_provider(self, manager: JWTTokenManager, request: Request) -> IdProvider:
        """Возвращает провайдер идентификаторов."""
        return TokenIdProvider(manager, request)

    user_gateway = provide(
        UserGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            UserSaver,
            UserReader,
            UserDeleter,
            UserUpdater,
            UserGatewayWithReaderAndDeleter,
            UserGatewayWithReaderAndSaver,
        ],
    )
    tag_gateway = provide(
        TagGateway,
        scope=Scope.REQUEST,
        provides=TagReader,
    )
    specialization_gateway = provide(
        SpecializationGateway,
        scope=Scope.REQUEST,
        provides=SpecializationReader,
    )
    city_gateway = provide(
        CityGateway,
        scope=Scope.REQUEST,
        provides=CityReader,
    )
    showcase_gateway = provide(
        ShowcaseGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            ShowcaseSaver,
            ShowcaseDeleter,
            ShowcaseReader,
            ShowcaseGatewayWithReaderAndDeleter,
        ],
    )
    register_user_interactor = provide(
        RegisterUserInteractor,
        scope=Scope.REQUEST,
    )
    auth_user_interactor = provide(
        AuthUserInteractor,
        scope=Scope.REQUEST,
    )
    read_user_interactor = provide(
        ReadUserInteractor,
        scope=Scope.REQUEST,
    )
    update_user_interactor = provide(
        UpdateUserInteractor,
        scope=Scope.REQUEST,
    )
    delete_user_interactor = provide(
        DeleteUserInteractor,
        scope=Scope.REQUEST,
    )
    read_tag_interactor = provide(
        ReadTagsInteractor,
        scope=Scope.REQUEST,
    )
    read_specializations_interactor = provide(
        ReadSpecializationsInteractor,
        scope=Scope.REQUEST,
    )
    read_cities_interactor = provide(
        ReadCitiesInteractor,
        scope=Scope.REQUEST,
    )
    transaction_manager = provide(
        SQLTransactionManager,
        scope=Scope.REQUEST,
        provides=TransactionManager,
    )
    password_hasher = provide(
        FakePasswordHasher,
        scope=Scope.REQUEST,
        provides=PasswordHasher,
    )
