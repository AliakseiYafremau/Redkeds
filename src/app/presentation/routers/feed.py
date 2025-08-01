from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.showcase import ReadShowcaseDTO
from app.application.interactors.recommendation_feed.read import ReadRecommendationFeed

feed_router = APIRouter(prefix="/feed", tags=["Работа с лентой рекомендаций"])


@feed_router.get("/")
@inject
async def read_feed(
    interactor: FromDishka[ReadRecommendationFeed],
) -> list[ReadShowcaseDTO]:
    """Возвращает ленту из витрин пользователей."""
    return await interactor()
