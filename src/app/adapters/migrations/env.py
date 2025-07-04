import asyncio
import os

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from app.adapters.database import build_database_url
from app.adapters.models import Base

config = context.config
target_metadata = Base.metadata


def get_database_url() -> str:
    """Получает и собирает URL для подключения к базе данных из переменных окружения."""
    login = os.environ.get("POSTGRES_LOGIN")
    password = os.environ.get("POSTGRES_PASSWORD")
    host = os.environ.get("POSTGRES_HOST")
    port = os.environ.get("POSTGRES_PORT")
    database = os.environ.get("POSTGRES_NAME")

    if not all([login, password, host, port, database]):
        raise RuntimeError("Не все переменные окружения для базы данных заданы!")

    return build_database_url(login, password, host, port, database)


def run_migrations_offline() -> None:
    """Запуск миграций в оффлайн-режиме."""
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Конфигурирует и запускает миграции."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations():
    """Асинхронный запуск миграций."""
    url = get_database_url()
    section = config.get_section(config.config_ini_section)
    section["sqlalchemy.url"] = url

    connectable = async_engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


def run_migrations_online() -> None:
    """Запуск миграций в онлайн-режиме (асинхронный)."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
