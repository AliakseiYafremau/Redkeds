import json
from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.adapters.exceptions import (
    AuthenticationError,
    UserDoesNotExistError,
)
from app.adapters.id_provider import JWTTokenManager, Token
from app.application.dto.user import LoginUserDTO, NewUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.application.interactors.user.register import RegisterUserInteractor
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user import NameDisplay

auth_router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Регистрация"],
)


@auth_router.post("/register")
@inject
async def register(  # noqa: PLR0913
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[RegisterUserInteractor],
    email: Annotated[str, Form()],
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    description: Annotated[str, Form()],
    name_display: Annotated[NameDisplay, Form()] = NameDisplay.USERNAME,
    city: Annotated[str, Form()] = '{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}',
    tags: Annotated[str, Form()] = '[{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}]',
    communication_method: Annotated[
        str, Form()
    ] = '{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}',
    specializations: Annotated[
        str, Form()
    ] = '[{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}]',
    nickname: Annotated[str | None, Form()] = None,
    status: Annotated[str | None, Form()] = None,
    photo: Annotated[UploadFile | None, File()] = None,
) -> Token:
    """Регистрация нового пользователя."""
    try:
        specialization_list = [
            SpecializationId(spec["id"]) for spec in json.loads(specializations)
        ]
        city_id = CityId(json.loads(city)["id"])
        tags_list = [TagId(tag["id"]) for tag in json.loads(tags)]
        communication_method_id = CommunicationMethodId(
            json.loads(communication_method)["id"]
        )
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Неправильные входные данные: {e}")

    photo_bytes = None
    if photo:
        photo_bytes = await photo.read()

    user_dto = NewUserDTO(
        email=email,
        username=username,
        password=password,
        specialization=specialization_list,
        city=city_id,
        description=description,
        tags=tags_list,
        communication_method=communication_method_id,
        nickname=nickname,
        photo=photo_bytes,
        status=status,
        name_display=name_display,
    )
    user_id = await interactor(user_dto)
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
