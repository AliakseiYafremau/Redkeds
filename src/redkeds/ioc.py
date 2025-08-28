from collections.abc import AsyncIterable
from uuid import uuid4

from dishka import AnyOf, Provider, Scope, provide
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from redkeds.adapters.database import new_async_engine, new_session_maker
from redkeds.adapters.file_manager import LocalFileManager
from redkeds.adapters.gateways.chat import ChatGateway, ChatMessageGateway
from redkeds.adapters.gateways.city import CityGateway
from redkeds.adapters.gateways.communication_method import CommunicationMethodGateway
from redkeds.adapters.gateways.like import LikeGateway
from redkeds.adapters.gateways.showcase import ShowcaseGateway, WorkGateway
from redkeds.adapters.gateways.skip import SkipGateway
from redkeds.adapters.gateways.specialization import SpecializationGateway
from redkeds.adapters.gateways.tag import TagGateway
from redkeds.adapters.gateways.user import DefaultPhotoGateway, UserGateway
from redkeds.adapters.id_provider import JWTTokenManager, TokenIdProvider
from redkeds.adapters.password import BcryptPasswordHasher
from redkeds.adapters.transaction import SQLTransactionManager
from redkeds.application.interactors.chat.create import CreateChatInteractor
from redkeds.application.interactors.chat.delete import (
    ChatGateway as ChatGatewayWithReaderAndDeleter,
)
from redkeds.application.interactors.chat.delete import DeleteChatInteractor
from redkeds.application.interactors.chat.messages.delete import (
    ChatMessageGateway as ChatMessageGatewayWithDeleterAndReader,
)
from redkeds.application.interactors.chat.messages.delete import (
    DeleteChatMessageInteractor,
)
from redkeds.application.interactors.chat.messages.read import ReadMessageInteractor
from redkeds.application.interactors.chat.messages.send import SendChatMessageInteractor
from redkeds.application.interactors.chat.read import ReadUserChatInteractor
from redkeds.application.interactors.city.read import ReadCitiesInteractor
from redkeds.application.interactors.communication_method.read import (
    ReadCommunicationMethodsInteractor,
)
from redkeds.application.interactors.file.read import ReadFileInteractor
from redkeds.application.interactors.like.add_like import AddLikeInteractor
from redkeds.application.interactors.like.delete_like import DeleteLikeInteractor
from redkeds.application.interactors.like.delete_like import (
    LikeGateway as LikeGatewayWithDeleterAndReader,
)
from redkeds.application.interactors.recommendation_feed.read import (
    ReadRecommendationFeed,
)
from redkeds.application.interactors.skip.add_skip import AddSkipInteractor
from redkeds.application.interactors.skip.delete_skip import DeleteSkipInteractor
from redkeds.application.interactors.skip.delete_skip import (
    SkipGateway as SkipGatewayWithDeleterAndReader,
)
from redkeds.application.interactors.specialization.read import (
    ReadSpecializationsInteractor,
)
from redkeds.application.interactors.tag.read import ReadTagsInteractor
from redkeds.application.interactors.user.auth import AuthUserInteractor
from redkeds.application.interactors.user.default_photo.read import (
    ReadDefaultPhotoInteractor,
)
from redkeds.application.interactors.user.delete import DeleteUserInteractor
from redkeds.application.interactors.user.delete import (
    ShowcaseGateway as ShowcaseGatewayWithReaderAndDeleter,
)
from redkeds.application.interactors.user.delete import (
    UserGateway as UserGatewayDeleterAndReader,
)
from redkeds.application.interactors.user.read import ReadUserInteractor
from redkeds.application.interactors.user.register import RegisterUserInteractor
from redkeds.application.interactors.user.register import (
    UserGateway as UserGatewayWithReaderAndSaver,
)
from redkeds.application.interactors.user.update import UpdateUserInteractor
from redkeds.application.interactors.user.update import (
    UserGateway as UserGatewayWithReaderAndUpdater,
)
from redkeds.application.interactors.work.create import CreateWorkInteractor
from redkeds.application.interactors.work.delete import DeleteWorkInteractor
from redkeds.application.interactors.work.delete import (
    WorkGateway as WorkGatewayWithDeleterAndReader,
)
from redkeds.application.interactors.work.read import (
    ReadAllWorksInteractor,
    ReadWorkInteractor,
)
from redkeds.application.interactors.work.update import UpdateWorkInteractor
from redkeds.application.interactors.work.update import (
    WorkGateway as WorkGatewayWithUpdaterAndReader,
)
from redkeds.application.interfaces.chat.chat_gateway import (
    ChatDeleter,
    ChatReader,
    ChatSaver,
)
from redkeds.application.interfaces.chat.chat_message_gateway import (
    ChatMessageDeleter,
    ChatMessageReader,
    ChatMessageSaver,
)
from redkeds.application.interfaces.city.city_gateway import CityReader
from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.common.uuid_generator import UUIDGenerator
from redkeds.application.interfaces.communication_method.communication_method_gateway import (  # noqa: E501
    CommunicationMethodReader,
)
from redkeds.application.interfaces.like.like_gateway import LikeDeleter, LikeSaver
from redkeds.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
    ShowcaseSaver,
)
from redkeds.application.interfaces.showcase.work_gateway import WorkReader, WorkSaver
from redkeds.application.interfaces.skip.skip_gateway import SkipDeleter, SkipSaver
from redkeds.application.interfaces.specialization.specialization_gateway import (
    SpecializationReader,
)
from redkeds.application.interfaces.tag.tag_gateway import TagReader
from redkeds.application.interfaces.user.default_photo_gateway import DefaultPhotoReader
from redkeds.application.interfaces.user.password_manager import PasswordHasher
from redkeds.application.interfaces.user.user_gateway import (
    UserDeleter,
    UserReader,
    UserSaver,
    UserUpdater,
)
from redkeds.config import (
    MediaConfig,
    PostgresConfig,
    TokenConfig,
    load_media_config,
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

    @provide(scope=Scope.APP)
    def get_postgres_config(self) -> PostgresConfig:
        """Возвращает конфигурацию подключения к PostgreSQL."""
        return load_postgres_config()

    @provide(scope=Scope.APP)
    def get_token_config(self) -> TokenConfig:
        """Возвращает конфигурацию для токенов."""
        return load_token_config()

    @provide(scope=Scope.APP)
    def get_media_config(self) -> MediaConfig:
        """Возвращает конифигурацию для медиа."""
        return load_media_config()

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
        UserGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            UserSaver,
            UserReader,
            UserDeleter,
            UserUpdater,
            UserGatewayWithReaderAndUpdater,
            UserGatewayDeleterAndReader,
            UserGatewayWithReaderAndSaver,
        ],
    )
    tag_gateway = provide(
        TagGateway,
        scope=Scope.REQUEST,
        provides=TagReader,
    )
    communication_method_gateway = provide(
        CommunicationMethodGateway,
        scope=Scope.REQUEST,
        provides=CommunicationMethodReader,
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
    like_gateway = provide(
        LikeGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            LikeSaver,
            LikeDeleter,
            LikeGatewayWithDeleterAndReader,
        ],
    )
    skip_gateway = provide(
        SkipGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            SkipSaver,
            SkipDeleter,
            SkipGatewayWithDeleterAndReader,
        ],
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
    work_gateway = provide(
        WorkGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            WorkReader,
            WorkSaver,
            WorkGatewayWithUpdaterAndReader,
            WorkGatewayWithDeleterAndReader,
        ],
    )
    chat_gateway = provide(
        ChatGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            ChatSaver, ChatDeleter, ChatReader, ChatGatewayWithReaderAndDeleter
        ],
    )
    chat_message_gateway = provide(
        ChatMessageGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[
            ChatMessageSaver,
            ChatMessageDeleter,
            ChatMessageReader,
            ChatMessageGatewayWithDeleterAndReader,
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
    read_default_photo_interactor = provide(
        ReadDefaultPhotoInteractor,
        scope=Scope.REQUEST,
    )
    read_tag_interactor = provide(
        ReadTagsInteractor,
        scope=Scope.REQUEST,
    )
    read_communication_method_interactor = provide(
        ReadCommunicationMethodsInteractor,
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
    read_work_interactor = provide(
        ReadWorkInteractor,
        scope=Scope.REQUEST,
    )
    read_all_works_interactor = provide(
        ReadAllWorksInteractor,
        scope=Scope.REQUEST,
    )
    create_work_interactor = provide(
        CreateWorkInteractor,
        scope=Scope.REQUEST,
    )
    update_work_interactor = provide(
        UpdateWorkInteractor,
        scope=Scope.REQUEST,
    )
    delete_work_interactor = provide(
        DeleteWorkInteractor,
        scope=Scope.REQUEST,
    )
    read_feed_interactor = provide(
        ReadRecommendationFeed,
        scope=Scope.REQUEST,
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
    chat_create_interactor = provide(
        CreateChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_delete_interactor = provide(
        DeleteChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_read_interactor = provide(
        ReadUserChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_delete_interactor = provide(
        DeleteChatMessageInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_read_interactor = provide(
        ReadMessageInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_send_interactor = provide(
        SendChatMessageInteractor,
        scope=Scope.REQUEST,
    )
    file_interactor = provide(
        ReadFileInteractor,
        scope=Scope.REQUEST,
    )
    add_like_interactor = provide(
        AddLikeInteractor,
        scope=Scope.REQUEST,
    )
    delete_like_interactor = provide(
        DeleteLikeInteractor,
        scope=Scope.REQUEST,
    )
    add_skip_interactor = provide(
        AddSkipInteractor,
        scope=Scope.REQUEST,
    )
    delete_skip_interactor = provide(
        DeleteSkipInteractor,
        scope=Scope.REQUEST,
    )
    default_photo_provider = provide(
        DefaultPhotoGateway,
        scope=Scope.REQUEST,
        provides=DefaultPhotoReader,
    )
