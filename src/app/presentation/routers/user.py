from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.adapters.exceptions import ShowcaseDoesNotExistError, UserDoesNotExistError
from app.application.dto.user import UpdateUserDTO, UserDTO
from app.application.interactors.user.delete import DeleteUserInteractor
from app.application.interactors.user.read import ReadUserInteractor
from app.application.interactors.user.update import UpdateUserInteractor

user_router = APIRouter(
    prefix="/user",
    tags=["Пользователь"],
)


@user_router.get("/")
@inject
async def read_user(
    interactor: FromDishka[ReadUserInteractor],
) -> UserDTO:
    """Получение информации о текущем пользователе."""
    try:
        return await interactor()
    except UserDoesNotExistError:
        raise HTTPException(
            status_code=404,
            detail="Пользователь не найден.",
        )


@user_router.patch("/")
@inject
async def update_user(
    user_data: UpdateUserDTO,
    interactor: FromDishka[UpdateUserInteractor],
) -> None:
    """Обновление пользователя."""
    try:
        await interactor(user_data)
    except UserDoesNotExistError:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")


@user_router.delete("/")
@inject
async def delete_user(
    interactor: FromDishka[DeleteUserInteractor],
) -> None:
    """Удаление пользователя."""
    try:
        await interactor()
    except (UserDoesNotExistError, ShowcaseDoesNotExistError):
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
