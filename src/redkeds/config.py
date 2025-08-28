from dataclasses import dataclass
from os import environ
from pathlib import Path


def get_env_variable(name: str) -> str:
    """Получает значение переменной окружения.

    Выбрасывает исключение,
    если она не установлена.
    """
    value = environ.get(name)
    if value is None:
        raise ValueError(f"Укажите {name} в переменное окружение.")
    return value


@dataclass
class PostgresConfig:
    """Конфигурация подключения к PostgreSQL."""

    login: str
    password: str
    host: str
    port: int
    name: str


@dataclass
class TokenConfig:
    """Конфигурация для токенов."""

    secret_key: str
    expire_time: int
    algorithm: str


@dataclass
class MediaConfig:
    """Конфигурация для управления медиа."""

    media_directory: Path


def load_postgres_config() -> PostgresConfig:
    """Загружает конфигурацию PostgreSQL из переменных окружения."""
    return PostgresConfig(
        login=get_env_variable("POSTGRES_LOGIN"),
        password=get_env_variable("POSTGRES_PASSWORD"),
        host=get_env_variable("POSTGRES_HOST"),
        port=int(get_env_variable("POSTGRES_PORT")),
        name=get_env_variable("POSTGRES_NAME"),
    )


def load_token_config() -> TokenConfig:
    """Загружает конфигурацию для токенов."""
    return TokenConfig(
        secret_key=get_env_variable("SECRET_KEY"),
        expire_time=int(get_env_variable("EXPIRE_TIME")),
        algorithm=get_env_variable("ALGORITHM"),
    )


def load_media_config() -> MediaConfig:
    """Загружает конфигурацию для медиа."""
    return MediaConfig(
        media_directory=Path(get_env_variable("MEDIA_DIR")),
    )
