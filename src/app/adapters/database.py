from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def new_session_maker(
    login: str,
    password: str,
    host: str,
    port: int,
    database: str,
) -> async_sessionmaker[AsyncSession]:
    """Create a new async session maker for connecting to the PostgreSQL database."""
    database_url = (
        f"postgresql+psycopg://{login}:{password}@{host}:{port}/{database}"
    )

    engine = create_async_engine(
        database_url,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return async_sessionmaker(
        engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
    )
