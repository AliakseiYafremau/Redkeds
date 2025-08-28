from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from redkeds.application.interactors.like.add_like import AddLikeInteractor
from redkeds.application.interactors.like.delete_like import DeleteLikeInteractor
from redkeds.domain.entities.like import LikeId
from redkeds.domain.entities.showcase import ShowcaseId

like_router = APIRouter(
    prefix="/like",
    tags=["Лайки"],
)


@like_router.post(
    path="/",
    summary="Постановка лайка.",
    description="Ставит лайкает на указанную витрину.",
)
@inject
async def add_like(
    showcase_id: ShowcaseId,
    interactor: FromDishka[AddLikeInteractor],
) -> LikeId:
    """Добавелние лойка."""
    return await interactor(showcase_id)


@like_router.delete(
    path="/", summary="Удаление лайка.", description="Убирает лайк с указанной витрины."
)
@inject
async def delete_like(
    like_id: LikeId,
    interactor: FromDishka[DeleteLikeInteractor],
) -> None:
    """Удаление лайка."""
    await interactor(like_id)
