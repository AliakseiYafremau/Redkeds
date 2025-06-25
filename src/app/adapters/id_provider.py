from typing import Protocol
from uuid import UUID

from fastapi import HTTPException, Request

from app.adapters.exceptions import AuthenticationError
from app.application.interfaces.common.id_provider import IdProvider
from app.domain.entities.user_id import UserId


class TokenManager(Protocol):
    """Интерфейс менеджера токенов."""

    def create_token(self, user_id: UserId) -> str:
        """Создает токен для пользователя."""
        ...

    def validate_token(self, token: str) -> UserId:
        """Проверяет токен и возвращает ID пользователя."""
        ...


class FakeTokenManager(TokenManager):
    """Фейковый менеджер токенов."""

    def create_token(self, user_id: UserId) -> str:
        """Создает фейковый токен для пользователя."""
        return f"fake-token-for-{user_id}"

    def validate_token(self, token: str) -> UserId:
        """Проверяет фейковый токен и возвращает ID пользователя."""
        if not token or not token.startswith("fake-token-for-"):
            raise AuthenticationError
        user_id_str = token[len("fake-token-for-") :]
        try:
            user_id = UUID(user_id_str)
        except ValueError:
            raise AuthenticationError
        return UserId(user_id)


class FakeIdProvider(IdProvider):
    """Фейковый провайдер для получения ID."""

    def __init__(self, token_manager: TokenManager, request: Request) -> None:
        self.token_manager = token_manager
        self.token = request.headers.get("token", "")

    def __call__(self) -> UserId:
        """Просто возвращает тот же ID."""
        try:
            user_id = self.token_manager.validate_token(self.token)
        except AuthenticationError:
            raise HTTPException(
                status_code=401,
                detail="Invalid or missing authentication token.",
            )
        return user_id
