from dishka import Provider, Scope, provide

from redkeds.main.config import (
    MediaConfig,
    PostgresConfig,
    TokenConfig,
    load_media_config,
    load_postgres_config,
    load_token_config,
)


class ConfigProvider(Provider):
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
