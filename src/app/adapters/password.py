from app.adapters.exceptions import InvalidPasswordError
from app.application.interfaces.user.password_manager import PasswordHasher


class FakePasswordHasher(PasswordHasher):
    """Интерфейс для хеширования паролей."""

    def hash_password(self, password: str) -> str:
        """Хеширует пароль."""
        return password

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Проверяет пароль."""
        if password == hashed_password:
            return True
        raise InvalidPasswordError
