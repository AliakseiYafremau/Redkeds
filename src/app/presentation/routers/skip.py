from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.interactors.skip.add_skip import AddSkipInteractor
from app.application.interactors.skip.delete_skip import DeleteSkipInteractor
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.skip import SkipId


skip_router = APIRouter(
    prefix="/skip",
    tags=["Скипы"],
)


@skip_router.get(
    path="/",
    summary="Постановка скипа.",
    description="Ставит скип на указанную витрину.",
)
@inject
async def add_skip(
        showcase_id: ShowcaseId,
        interactor: FromDishka[AddSkipInteractor],
) -> SkipId:
    """Добавелние скипа."""
    return await interactor(showcase_id)


@skip_router.delete(
    path="/", summary="Удаляет скип.", description="Убирает скип с указанной витрины"
)
@inject
async def delete_skip(
    skip_id: SkipId,
    interactor: FromDishka[DeleteSkipInteractor],
) -> None:
    """Удаление скипа."""
    await interactor(skip_id)
