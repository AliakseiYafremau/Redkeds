import json
from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.adapters.exceptions import TargetNotFoundError
from app.adapters.id_provider import JWTTokenManager, Token
from app.application.dto.user import LoginUserDTO, NewUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.application.interactors.user.register import RegisterUserInteractor
from app.application.interactors.user.unique_login import UniqueLoginInteractor
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.file_id import FileId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user import NameDisplay

auth_router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация и Регистрация"],
)


@auth_router.post(
    path="/register",
    summary="Регистрация пользователя.",
    description=(
        "Регистрация пользователя происходит по *E-mail* и *паролю*. \n\n"
        "Пароль должен содержать не менее **5 символов** и как минимум **одну цифру** "
        "и **одну букву**. \n\n"
        "Поля **фото**, **статус**, **ник**, **город**, **способ общения** "
        "являются не обязательными."
    ),
    deprecated=True,
)
@inject
async def register(  # noqa: PLR0913
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[RegisterUserInteractor],
    email: Annotated[str, Form(description="Почта пользователя.")],
    username: Annotated[str, Form(description="Имя пользователя.")],
    password: Annotated[str, Form(description="Пароль.")],
    description: Annotated[str, Form(description='Краткое описание "О себе".')],
    name_display: Annotated[NameDisplay, Form()] = NameDisplay.USERNAME,
    city: Annotated[
        str, Form(description="Город.")
    ] = '{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}',
    tags: Annotated[
        str,
        Form(
            description=(
                "Цель пользователя. Указывает на то, в чем заинтересован "
                'пользователь ("собираю команду", "ищу друзей")'
            )
        ),
    ] = '[{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}]',
    communication_method: Annotated[
        str,
        Form(
            description=(
                "Метод общения, предпочитаемый пользователем "
                "(только онлайн, готов к встречам)."
            )
        ),
    ] = '{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}',
    specializations: Annotated[
        str, Form(description='Специализация пользователя ("веб-дизайнер", "художник")')
    ] = '[{"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}]',
    nickname: Annotated[
        str | None,
        Form(
            description=(
                "Уникальный никнейм пользователя, который он может указать при желании."
            )
        ),
    ] = None,
    status: Annotated[
        str | None, Form(description="Текущий статус пользователя.")
    ] = None,
    photo: Annotated[bytes | None, File(description="Фото пользователя.")] = None,
) -> Token:
    """Регистрация пользователя."""
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
        photo=photo,
        status=status,
        name_display=name_display,
    )
    user_id = await interactor(user_dto)
    return token_manager.create_token(user_id)


@auth_router.post(
    path="/login",
    summary="Аутентификация пользователя.",
    description="Аутентификация пользователя происходит по его *E-mail* и *паролю*.",
)
@inject
async def login(
    user_data: LoginUserDTO,
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[AuthUserInteractor],
) -> Token:
    """Вход пользователя."""
    user_id = await interactor(user_data)
    return token_manager.create_token(user_id)


@auth_router.post(
    path="/v2/register",
    summary="Регистрация пользователя.",
    description=(
        "Регистрация пользователя происходит по *E-mail* и *паролю*. \n\n"
        "Пароль должен содержать не менее **5 символов** и как минимум **одну цифру** "
        "и **одну букву**. \n\n"
        "Поля **photo**, **status**, **nickname** "
        "являются не обязательными. "
        "При пропуске поля **tags** и **specializations**, "
        "пользователю не назначаются цели и специализации соответственно. \n\n"
    ),
)
@inject
async def register_v2(  # noqa: PLR0913
    token_manager: FromDishka[JWTTokenManager],
    interactor: FromDishka[RegisterUserInteractor],
    email: Annotated[str, Form(description="Почта пользователя.")],
    username: Annotated[str, Form(description="Имя пользователя.")],
    password: Annotated[str, Form(description="Пароль.")],
    description: Annotated[str, Form(description="Краткое описание 'О себе'.")],
    city: Annotated[CityId, Form(description="Город.")],
    communication_method: Annotated[
        CommunicationMethodId, Form(description="Метод общения.")
    ],
    tags: Annotated[list[TagId], Form(description="Цели пользователя.")],
    specializations: Annotated[
        list[SpecializationId], Form(description="Специализации пользователя.")
    ],
    name_display: Annotated[
        NameDisplay,
        Form(
            description=(
                "Выбор отображения между именем (username) и ником (nickname)."
                " По умолчанию устанавливается имя."
            )
        ),
    ] = NameDisplay.USERNAME,
    nickname: Annotated[str | None, Form(description="Никнейм пользователя.")] = None,
    status: Annotated[
        str | None, Form(description="Текущий статус пользователя.")
    ] = None,
    photo: Annotated[UploadFile | None, File(description="Фото пользователя.")] = None,
) -> Token:
    """Регистрация пользователя."""
    user_dto = NewUserDTO(
        email=email,
        username=username,
        password=password,
        specialization=specializations,
        city=city,
        description=description,
        tags=tags,
        communication_method=communication_method,
        nickname=nickname,
        photo=await photo.read(),
        default_photo=None,
        status=status,
        name_display=name_display,
    )
    user_id = await interactor(user_dto)
    return token_manager.create_token(user_id)


@auth_router.post("/verify_login")
@inject
async def verify_unique_login(
    interactor: FromDishka[UniqueLoginInteractor],
    email: str,
) -> bool:
    """Проверка уникальности логина."""
    try:
        return await interactor(email)
    except TargetNotFoundError:
        return False
