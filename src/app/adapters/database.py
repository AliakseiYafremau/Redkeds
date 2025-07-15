from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def build_database_url(
    login: str,
    password: str,
    host: str,
    port: int,
    database: str,
) -> str:
    """Собирает URL подключения к базе данных."""
    return f"postgresql+psycopg://{login}:{password}@{host}:{port}/{database}"


def new_async_engine(
    login: str,
    password: str,
    host: str,
    port: int,
    database: str,
) -> AsyncEngine:
    """Создает новый async engine для работы с базой данных PostgreSQL."""
    database_url = build_database_url(login, password, host, port, database)
    return create_async_engine(
        database_url,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )


def new_session_maker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """Создаёт новый async session maker для подключения к базе данных PostgreSQL."""
    return async_sessionmaker(
        engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
    )
