from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.work import NewWorkDTO, ReadWorkDTO, UpdateWorkDTO
from app.application.interactors.work.create import CreateWorkInteractor
from app.application.interactors.work.delete import DeleteWorkInteractor
from app.application.interactors.work.read import (
    ReadAllWorksInteractor,
    ReadWorkInteractor,
)
from app.application.interactors.work.update import UpdateWorkInteractor
from app.domain.entities.showcase import ShowcaseId, WorkId

work_router = APIRouter(prefix="/work", tags=["Работа витрин"])


@work_router.get("/{work_id}")
@inject
async def read_work(
    work_id: WorkId,
    interactor: FromDishka[ReadWorkInteractor],
) -> ReadWorkDTO:
    """Получение информации о работе по ее ID."""
    return await interactor(work_id)


@work_router.get("/all/{showcase_id}")
@inject
async def read_all_works(
    showcase_id: ShowcaseId,
    interactor: FromDishka[ReadAllWorksInteractor],
) -> list[ReadWorkDTO]:
    """Получение информации о всех работах витрины по ID."""
    return await interactor(showcase_id)


@work_router.post("/")
@inject
async def create_work(
    work_data: NewWorkDTO,
    interactor: FromDishka[CreateWorkInteractor],
) -> None:
    """Создание новой работы витрины."""
    await interactor(work_data)


@work_router.patch("/")
@inject
async def update_work(
    work_data: UpdateWorkDTO,
    interactor: FromDishka[UpdateWorkInteractor],
) -> None:
    """Обновление работы витрины."""
    await interactor(work_data)


@work_router.delete("/{work_id}")
@inject
async def delete_work(
    work_id: WorkId,
    interactor: FromDishka[DeleteWorkInteractor],
) -> None:
    """Удаление работы витрины."""
    await interactor(work_id)
