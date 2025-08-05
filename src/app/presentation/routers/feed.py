from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Query

from app.application.dto.showcase import ReadShowcaseDTO
from app.application.interactors.recommendation_feed.read import ReadRecommendationFeed
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId

feed_router = APIRouter(prefix="/feed", tags=["Работа с лентой рекомендаций"])


@feed_router.get("/")
@inject
async def read_feed(
    interactor: FromDishka[ReadRecommendationFeed],
    specialization_ids: Annotated[list[SpecializationId] | None, Query()] = None,
    city_ids: Annotated[list[CityId] | None, Query()] = None,
    tag_ids: Annotated[list[TagId] | None, Query()] = None,
    communication_method_ids: Annotated[
        list[CommunicationMethodId] | None, Query()
    ] = None,
) -> list[ReadShowcaseDTO]:
    """Возвращает ленту из витрин пользователей."""
    return await interactor(
        specialization_ids, city_ids, tag_ids, communication_method_ids
    )
