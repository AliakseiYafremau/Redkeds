from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.tag import TagDTO
from app.application.interactors.tag.read import ReadTagsInteractor

tag_router = APIRouter()


@tag_router.get("/")
@inject
async def tags(interactor: FromDishka[ReadTagsInteractor]) -> list[TagDTO]:
    """Получает список тегов."""
    return await interactor()
