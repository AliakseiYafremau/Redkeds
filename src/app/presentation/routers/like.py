from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.like import NewLikeDTO
from app.application.interactors.like.add_like import AddLikeInteractor
from app.application.interactors.like.delete_like import DeleteLikeInteractor
from app.domain.entities.like import LikeId

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
    like_data: NewLikeDTO,
    interactor: FromDishka[AddLikeInteractor],
) -> LikeId:
    """Добавелние лойка."""
    return await interactor(like_data)


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
