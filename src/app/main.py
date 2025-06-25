import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import Depends, FastAPI, Header

from app.ioc import AppProvider
from app.presentation.routers.auth import auth_router
from app.presentation.routers.tag import tag_router


def common_headers(token: str = Header(None)):
    return token

def get_app() -> FastAPI:
    """Создает и настраивает приложение FastAPI."""
    container = make_async_container(AppProvider(), FastapiProvider())
    app = FastAPI(
        title="Redkeds",
        dependencies=[
            Depends(common_headers)
        ],
    )
    app.include_router(tag_router)
    app.include_router(auth_router)
    setup_dishka(container, app)
    return app


def run() -> None:
    """Запускает приложение."""
    uvicorn.run(get_app())
