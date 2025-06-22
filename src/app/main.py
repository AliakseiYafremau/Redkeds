import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import FromDishka, inject, setup_dishka
from fastapi import FastAPI

from app.application.dto.tag import TagDTO
from app.application.interactors.tag.read import ReadTagsInteractor
from app.ioc import AppProvider

app = FastAPI()


@app.get("/")
@inject
async def tags(interactor: FromDishka[ReadTagsInteractor]) -> list[TagDTO]:
    """Получает список тегов."""
    return await interactor()


if __name__ == "__main__":
    container = make_async_container(AppProvider())
    setup_dishka(container, app)

    uvicorn.run(app)
