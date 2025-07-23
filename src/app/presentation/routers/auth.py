from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.adapters.exceptions import (
    AuthenticationError,
    CommunicationMethodDoesNotExistError,
    SpecializationDoesNotExistError,
    TagDoesNotExistError,
    UserAlreadyExistsError,
    UserDoesNotExistError,
)
from app.adapters.id_provider import JWTTokenManager, Token
from app.application.dto.user import LoginUserDTO, NewUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.application.interactors.user.register import RegisterUserInteractor
from app.domain.exceptions import WeakPasswordError
from sqlalchemy.exc import IntegrityError

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
    try:
        user_id = await interactor(user_data)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким именем уже существует.",
        )
    except WeakPasswordError:
        raise HTTPException(
            status_code=400,
            detail=(
                "Пароль не соответствует требованиям безопасности. "
                "Пароль должен содержать не менее 5 символов и "
                "как минимум одну букву и одну цифру"
            ),
        )
    except TagDoesNotExistError:
        raise HTTPException(
            status_code=400,
            detail=("Теги с таким ID не существуют."),
        )
    except SpecializationDoesNotExistError:
        raise HTTPException(
            status_code=400,
            detail=("Специализации с таким ID не существуют."),
        )
    except CommunicationMethodDoesNotExistError:
        raise HTTPException(
            status_code=400,
            detail=("Метод общения с таким ID не существует."),
        )
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Невалидные данные",
        )
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
