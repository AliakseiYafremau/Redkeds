from typing import Protocol


class PasswordHasher(Protocol):
    """Интерфейс для хеширования паролей."""

    def hash_password(self, password: str) -> str:
        """Хеширует пароль."""
        ...

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Проверяет пароль."""
        ...
