from uuid import uuid4

from fastapi import Request

from app.adapters.exceptions import AuthenticationError
from app.application.interfaces.common.id_provider import IdProvider
from app.domain.entities.user_id import UserId


class FakeIdProvider(IdProvider):
    """Фейковый провайдер для получения ID."""

    def __init__(self, request: Request) -> None:
        self.user_id = request.path_params.get("user_id", None)

    def __call__(self) -> UserId:
        """Просто возвращает тот же ID."""
        if self.user_id is None:
            raise AuthenticationError
        return UserId(uuid4())
