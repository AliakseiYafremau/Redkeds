from fastapi import Request
from fastapi.responses import JSONResponse

from app.adapters import exceptions as adapters_exc
from app.domain import exceptions as domain_exc

domain_exceptions: dict[type[Exception], tuple[int, str]] = {
    domain_exc.CannotCreateShowcaseError: (400, "Невозможно создать витрину."),
    domain_exc.CannotManageChatError: (400, "Невозможно управлять чатом."),
    domain_exc.CannotManageChatMessageError: (
        400,
        "Невозможно управлять сообщением чата.",
    ),
    domain_exc.CannotManageWorkError: (400, "Невозможно управлять работой витрины."),
    domain_exc.CannotUpdateWorkError: (400, "Невозможно обновить работу."),
    domain_exc.WeakPasswordError: (
        400,
        (
            "Пароль не соответствует требованиям безопасности. "
            "Пароль должен содержать не менее 5 символов и "
            "как минимум одну букву и одну цифру"
        ),
    ),
}

adapter_exceptions: dict[type[Exception], tuple[int, str]] = {
    adapters_exc.AuthenticationError: (400, "Неправильные входные данные."),
    adapters_exc.CommunicationMethodDoesNotExistError: (
        400,
        "Метод общения не существует.",
    ),
    adapters_exc.InvalidPasswordError: (400, "Неправильный пароль"),
    adapters_exc.ShowcaseDoesNotExistError: (400, "Витрина пользователя не существует"),
    adapters_exc.SpecializationDoesNotExistError: (400, "Специализация не существует."),
    adapters_exc.TagDoesNotExistError: (400, "Тег не существуют."),
    adapters_exc.UserAlreadyExistsError: (400, "Пользователь уже существует."),
    adapters_exc.UserDoesNotExistError: (400, "Пользователь не существует."),
    adapters_exc.WorkDoesNotExistError: (400, "Работа не существует."),
}


async def adapter_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    """Обработчик ошибок адптер слоя."""
    data = domain_exceptions.get(type(exc))
    if data is not None:
        status, message = data
        return JSONResponse(status_code=status, content={"detail": message})
    return JSONResponse(status_code=500, content={"detail": "Неизвестная ошибка."})


async def domain_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    """Обработчик ошибок адптер домена."""
    data = domain_exceptions.get(type(exc))
    if data is not None:
        status, message = data
        return JSONResponse(status_code=status, content={"detail": message})
    return JSONResponse(status_code=500, content={"detail": "Неизвестная ошибка."})
