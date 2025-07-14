import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader

from app.ioc import AppProvider
from app.presentation.routers.auth import auth_router
from app.presentation.routers.specialization import specialization_router
from app.presentation.routers.tag import tag_router
from app.presentation.routers.user import user_router


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
    setup_dishka(container, app)
    return app


def run() -> None:
    """Запускает приложение."""
    uvicorn.run("app.main:get_app", reload=True, factory=True)
