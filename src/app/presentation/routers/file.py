from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response

from app.application.interactors.file.read import ReadFileInteractor
from app.domain.entities.file_id import FileId

file_router = APIRouter(prefix="/file", tags=["Файлы"])


@file_router.get("/{file_id}")
@inject
async def read_file(
    file_id: FileId,
    interactor: FromDishka[ReadFileInteractor],
) -> bytes:
    """Получение файла по его ID."""
    file = await interactor(file_id)
    return Response(content=file)
