from fastapi import APIRouter
from uuid import UUID
from dishka.integrations.fastapi import FromDishka, inject

from app.application.dto.work import ReadWorkDTO, NewWorkDTO
from app.application.interactors.work.read import ReadWorkInteractor
from app.domain.entities.showcase import WorkId
from app.application.interactors.work.create import CreateWorkInteractor


work_router = APIRouter(
    prefix="/work",
    tags=["Работа витрин"]
)

@work_router.get("/{work_id}")
@inject
async def read_work(
    work_id: WorkId,
    interactor: FromDishka[ReadWorkInteractor],
) -> ReadWorkDTO:
    """Получение информации о работе по ее ID."""
    return await interactor(work_id)


@work_router.post("/")
@inject
async def create_work(
    data: NewWorkDTO,
    interactor: FromDishka[CreateWorkInteractor],
) -> None:
    """Создание новой работы витрины."""
    await interactor(data)
