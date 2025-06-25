from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.interactors.showcase.create import CreateShowcaseInteractor
from app.application.interactors.showcase.delete import DeleteShowcaseInteractor
from app.domain.entities.showcase import ShowcaseId

showcase_router = APIRouter(
    prefix="/showcase",
    tags=["Витрина пользователя"],
)


@showcase_router.post("/")
@inject
async def create_showcase(
    interactor: FromDishka[CreateShowcaseInteractor],
) -> ShowcaseId:
    """Создание витрины пользователя."""
    return await interactor()


@showcase_router.delete("/")
@inject
async def delete_showcase(
    interactor: FromDishka[DeleteShowcaseInteractor],
) -> None:
    """Удаление витрины пользователя."""
    return await interactor()
