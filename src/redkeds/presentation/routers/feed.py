from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Query

from redkeds.application.dto.showcase import ReadShowcaseDTO
from redkeds.application.interactors.recommendation_feed.read import (
    ReadRecommendationFeed,
)
from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId

feed_router = APIRouter(prefix="/feed", tags=["Лента рекомендаций"])


@feed_router.get(
    path="/",
    summary="Получение ленты рекомендаций.",
    description="Возвращает список витрин, основываясь на предпочтениях пользователя.",
)
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
