from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


def new_session_maker() -> async_sessionmaker[AsyncSession]:
    """Create a new async session maker for connecting to the PostgreSQL database."""
    database_url = (
        "postgresql+psycopg://{login}:{password}@{host}:{port}/{database}".format(
            login="postgres",
            password="1234",
            host="localhost",
            port=5432,
            database="postgres",
        )
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
