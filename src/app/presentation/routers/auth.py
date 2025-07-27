from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.adapters.exceptions import (
    AuthenticationError,
    UserDoesNotExistError,
)
from app.adapters.id_provider import JWTTokenManager, Token
from app.application.dto.user import LoginUserDTO, NewUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.application.interactors.user.register import RegisterUserInteractor

auth_router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Регистрация"],
)


@auth_router.post("/register")
@inject
async def register(
    user_data: NewUserDTO,
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[RegisterUserInteractor],
) -> Token:
    """Регистрация нового пользователя."""
    user_id = await interactor(user_data)
    return token_manager.create_token(user_id)


@auth_router.post("/login")
@inject
async def login(
    user_data: LoginUserDTO,
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[AuthUserInteractor],
) -> Token:
    """Вход пользователя."""
    try:
        user_id = await interactor(user_data)
    except (AuthenticationError, UserDoesNotExistError):
        raise HTTPException(
            status_code=400,
            detail=("Неправильные входные данные."),
        )
    return token_manager.create_token(user_id)
