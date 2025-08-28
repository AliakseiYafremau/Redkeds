from dataclasses import dataclass
from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, File, Form, UploadFile

from redkeds.application.dto.work import NewWorkDTO, ReadWorkDTO, UpdateWorkDTO
from redkeds.application.interactors.work.create import CreateWorkInteractor
from redkeds.application.interactors.work.delete import DeleteWorkInteractor
from redkeds.application.interactors.work.read import (
    ReadAllWorksInteractor,
    ReadWorkInteractor,
)
from redkeds.application.interactors.work.update import UpdateWorkInteractor
from redkeds.domain.entities.showcase import ShowcaseId, WorkId

work_router = APIRouter(prefix="/work", tags=["Работы витрин"])


@dataclass
class UpdateSchema:
    """Схема обновления работы."""

    work_id: WorkId
    title: str | None
    description: str | None


@work_router.get(
    path="/{work_id}",
    summary="Получение работы витрины.",
    description="Возвращает работу витрины по её ID.",
)
@inject
async def read_work(
    work_id: WorkId,
    interactor: FromDishka[ReadWorkInteractor],
) -> ReadWorkDTO:
    """Получение информации о работе по ее ID."""
    return await interactor(work_id)


@work_router.get(
    path="/all/{showcase_id}",
    summary="Получение работ витрины.",
    description="Получает все работы витрины по её ID.",
)
@inject
async def read_all_works(
    showcase_id: ShowcaseId,
    interactor: FromDishka[ReadAllWorksInteractor],
) -> list[ReadWorkDTO]:
    """Получение информации о всех работах витрины по ID."""
    return await interactor(showcase_id)


@work_router.post(
    path="/",
    summary="Сохранение работы витрины.",
    description="Сохраняет новую работу витрины пользователя.",
)
@inject
async def create_work(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    file: Annotated[UploadFile, File()],
    interactor: FromDishka[CreateWorkInteractor],
) -> None:
    """Создание новой работы витрины."""
    work_dto = NewWorkDTO(title=title, description=description, file=await file.read())
    await interactor(work_dto)


@work_router.patch(
    path="/",
    summary="Обновление работы витрины.",
    description="Обновляет информацию о работе витрины.",
)
@inject
async def update_work(
    work_data: UpdateSchema,
    interactor: FromDishka[UpdateWorkInteractor],
) -> None:
    """Обновление работы витрины."""
    work_dto = UpdateWorkDTO(
        work_id=work_data.work_id,
        title=work_data.title,
        description=work_data.description,
    )
    await interactor(work_dto)


@work_router.patch(
    path="/photo",
    summary="Замена файла работы витрины.",
    description="Заменяет файл работы витрины.",
)
@inject
async def update_work_photo(
    work_id: Annotated[WorkId, Form()],
    file: Annotated[bytes, File()],
    interactor: FromDishka[UpdateWorkInteractor],
) -> None:
    """Обновление файла работы."""
    work_dto = UpdateWorkDTO(
        work_id=work_id,
        file=file,
    )
    await interactor(work_dto)


@work_router.delete(
    path="/{work_id}",
    summary="Удаление работы витрины.",
    description="Удаляет работу витрины пользователя по её ID.",
)
@inject
async def delete_work(
    work_id: WorkId,
    interactor: FromDishka[DeleteWorkInteractor],
) -> None:
    """Удаление работы витрины."""
    await interactor(work_id)
