import datetime
from dataclasses import dataclass

import jwt
from fastapi import HTTPException, Request

from redkeds.adapters.exceptions import AuthenticationError
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.config import TokenConfig
from redkeds.domain.entities.user_id import UserId


@dataclass
class Token:
    """Схема для jwt-токена."""

    access_token: str


class JWTTokenManager:
    """Менеджер jwt-токенов."""

    def __init__(self, config: TokenConfig) -> None:
        self.secret_key = config.secret_key
        self.expire_time = config.expire_time
        self.algorithm = config.algorithm

    def create_token(self, user_id: UserId) -> Token:
        """Создает jwt-токен для пользователя."""
        payload = {
            "sub": str(user_id),
            "exp": (
                datetime.datetime.now(datetime.UTC)
                + datetime.timedelta(minutes=self.expire_time)
            ),
        }
        return Token(
            access_token=jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        )

    def validate_token(self, token: str) -> UserId:
        """Проверяет jwt-токен и возвращает ID пользователя."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return UserId(payload["sub"])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
            raise AuthenticationError("Invalid or expired token")


class TokenIdProvider(IdProvider):
    """Провайдер для получения ID."""

    def __init__(self, token_manager: JWTTokenManager, request: Request) -> None:
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
