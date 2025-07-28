import asyncio

import uvicorn
from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncEngine

from app.exception_handlers import setup_exception_handlers
from app.ioc import AppProvider
from app.presentation.routers.admin_panel import connect_admin_panel
from app.presentation.routers.auth import auth_router
from app.presentation.routers.chat import chat_router
from app.presentation.routers.city import city_router
from app.presentation.routers.feed import feed_router
from app.presentation.routers.file import file_router
from app.presentation.routers.messages import message_router
from app.presentation.routers.specialization import specialization_router
from app.presentation.routers.tag import tag_router
from app.presentation.routers.user import user_router
from app.presentation.routers.work import work_router


async def setup_admin_panel(app: FastAPI, container: AsyncContainer) -> None:
    """Настройка админ-панели."""
    async with container() as app_container:
        engine = await app_container.get(AsyncEngine)
        connect_admin_panel(app=app, engine=engine)


def get_app() -> FastAPI:
    """Создает и настраивает приложение FastAPI."""
    container = make_async_container(AppProvider(), FastapiProvider())
    app = FastAPI(
        title="Redkeds",
        dependencies=[
            Depends(APIKeyHeader(name="token", auto_error=False)),
        ],
    )
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(tag_router)
    app.include_router(specialization_router)
    app.include_router(city_router)
    app.include_router(work_router)
    app.include_router(feed_router)
    app.include_router(chat_router)
    app.include_router(file_router)
    app.include_router(message_router)

    setup_exception_handlers(app)

    asyncio.create_task(setup_admin_panel(app, container))  # noqa: RUF006

    setup_dishka(container, app)
    return app


def run() -> None:
    """Запускает приложение."""
    uvicorn.run("app.main:get_app", reload=True, factory=True)
