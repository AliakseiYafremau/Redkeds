from dataclasses import dataclass
from datetime import datetime
from os import environ


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
    expire_time: datetime
    algorithm: str


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
        expire_time=get_env_variable("EXPIRE_TIME"),
        algorithm=get_env_variable("ALGORITHM"),
    )
