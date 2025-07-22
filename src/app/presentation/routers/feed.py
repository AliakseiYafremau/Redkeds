from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.adapters.exceptions import (
    UserDoesNotExistError,
)
from app.application.dto.showcase import ReadShowcaseDTO
from app.application.interactors.recommendation_feed.read import ReadRecommendationFeed

feed_router = APIRouter(prefix="/feed", tags=["Работа с лентой рекомендаций"])


@feed_router.get("/")
@inject
async def read_feed(
    interactor: FromDishka[ReadRecommendationFeed],
) -> list[ReadShowcaseDTO]:
    """Возвращает ленту из витрин пользователей."""
    try:
        return await interactor()
    except UserDoesNotExistError:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
