from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.tag import TagDTO
from app.application.interactors.tag.read import ReadTagsInteractor

tag_router = APIRouter(
    prefix="/tags",
    tags=["Теги"],
)


@tag_router.get(
    path="/",
    summary="Получение всех тегов",
    description="Возвращает список всех тегов.",
)
@inject
async def get_tags(interactor: FromDishka[ReadTagsInteractor]) -> list[TagDTO]:
    """Получение список тегов."""
    return await interactor()
