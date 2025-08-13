from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app.adapters.exceptions import (
    AuthenticationError,
    InvalidPasswordError,
    TargetAlreadyExistError,
    TargetNotFoundError,
)
from app.domain.exceptions import AccessDeniedError, WeakPasswordError

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
    return JSONResponse(status_code=status, content={"detail": exc.args[0]})
