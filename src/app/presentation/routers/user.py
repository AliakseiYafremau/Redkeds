from dataclasses import asdict, dataclass
from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, File, UploadFile

from app.application.dto.user import UpdateUserDTO, UserDTO
from app.application.interactors.user.delete import DeleteUserInteractor
from app.application.interactors.user.read import ReadUserInteractor
from app.application.interactors.user.update import UpdateUserInteractor
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user import NameDisplay

user_router = APIRouter(
    prefix="/user",
    tags=["Пользователь"],
)


@dataclass
class UpdateSchema:
    """Схема для обновления пользователя."""

    email: str | None = None
    username: str | None = None
    nickname: str | None = None
    specialization: list[SpecializationId] | None = None
    city: CityId | None = None
    description: str | None = None
    tags: list[TagId] | None = None
    communication_method: CommunicationMethodId | None = None
    status: str | None = None
    showcase: ShowcaseId | None = None
    name_display: NameDisplay | None = None


@user_router.get(
    path="/",
    summary="Чтение пользователя.",
    description="Возвращает информацию о пользователе.",
)
@inject
async def read_user(
    interactor: FromDishka[ReadUserInteractor],
) -> UserDTO:
    """Получение информации о текущем пользователе."""
    return await interactor()


@user_router.patch(
    path="/",
    summary="Обновление пользователя.",
    description="Обновляет информацию о пользователе.",
)
@inject
async def update_user(
    user_data: UpdateSchema,
    interactor: FromDishka[UpdateUserInteractor],
) -> None:
    """Обновление пользователя."""
    user_dict = asdict(user_data)
    user_dto = UpdateUserDTO(**user_dict)
    await interactor(user_dto)


@user_router.patch(
    path="/photo",
    summary="Замена аватара.",
    description="Заменяет фото пользователя (аватар).",
)
@inject
async def update_user_photo(
    photo: Annotated[UploadFile, File()], interactor: FromDishka[UpdateUserInteractor]
) -> None:
    """Обновление фото пользователя."""
    user_dto = UpdateUserDTO(photo=await photo.read())
    await interactor(user_dto)


@user_router.delete(
    path="/", summary="Удаление пользователя.", description="Удаляет пользователя."
)
@inject
async def delete_user(
    interactor: FromDishka[DeleteUserInteractor],
) -> None:
    """Удаление пользователя."""
    await interactor()
