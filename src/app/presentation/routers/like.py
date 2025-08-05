from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.interactors.like.add_like import AddLikeInteractor
from app.application.interactors.like.delete_like import DeleteLikeInteractor
from app.domain.entities.like import LikeId

like_router = APIRouter(
    prefix="/like",
    tags=["Добавление и удаление лайков"],
)


@like_router.get("/")
@inject
async def add_like(
    interactor: FromDishka[AddLikeInteractor],
) -> LikeId:
    """Добавелние лойка."""
    return await interactor()


@like_router.delete("/")
@inject
async def delete_like(
    interactor: FromDishka[DeleteLikeInteractor],
) -> None:
    """Удаление лайка."""
    await interactor()
