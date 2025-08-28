from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Response

from redkeds.application.interactors.file.read import ReadFileInteractor
from redkeds.application.interactors.user.default_photo.read import (
    ReadDefaultPhotoInteractor,
)
from redkeds.domain.entities.file_id import FileId

file_router = APIRouter(prefix="/file", tags=["Файлы"])
default_photo_router = APIRouter(prefix="/default_photo", tags=["Файлы"])


@file_router.get(
    path="/{file_id}",
    summary="Загрузка файла.",
    description="Возвращает сохраненный файл по его ID.",
)
@inject
async def read_file(
    file_id: FileId,
    interactor: FromDishka[ReadFileInteractor],
) -> Response:
    """Получение файла по его ID."""
    file = await interactor(file_id)
    return Response(content=file)


@default_photo_router.get(
    path="/",
    summary="Получение фотографий по умолчанию.",
    description="Возвращает список фотографий по умолчанию.",
)
@inject
async def read_default_photos(
    interactor: FromDishka[ReadDefaultPhotoInteractor],
) -> list[FileId]:
    """Получение фотографий по умолчанию."""
    return await interactor()
