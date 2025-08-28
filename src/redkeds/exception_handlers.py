from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from redkeds.adapters.exceptions import (
    AuthenticationError,
    InvalidPasswordError,
    TargetAlreadyExistError,
    TargetNotFoundError,
)
from redkeds.domain.exceptions import AccessDeniedError, WeakPasswordError

exceptions: dict[type[Exception], int] = {
    AccessDeniedError: 401,
    TargetNotFoundError: 400,
    TargetAlreadyExistError: 400,
    WeakPasswordError: 400,
    AuthenticationError: 400,
    InvalidPasswordError: 400,
    IntegrityError: 400,
}


def setup_exception_handlers(app: FastAPI) -> None:
    """Добавляет обработчики ошибок в fastapi-приложение."""
    app.add_exception_handler(Exception, common_exception_handler)


async def common_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    """Обработчик ошибок."""
    status = exceptions.get(type(exc), 500)
    detail = exc.__class__.__name__
    if exc.args:
        detail += f": {exc.args[0]}"
    return JSONResponse(status_code=status, content={"detail": detail})
