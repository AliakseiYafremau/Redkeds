import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import FastAPI

from app.ioc import AppProvider
from app.presentation.routers.tag import tag_router


def get_app() -> FastAPI:
    """Создает и настраивает приложение FastAPI."""
    container = make_async_container(AppProvider(), FastapiProvider())
    app = FastAPI(title="Dishka Example App")
    app.include_router(tag_router)
    setup_dishka(container, app)
    return app


def run() -> None:
    """Запускает приложение."""
    uvicorn.run(get_app())
