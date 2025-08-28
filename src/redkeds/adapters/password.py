import bcrypt

from redkeds.adapters.exceptions import InvalidPasswordError
from redkeds.application.interfaces.user.password_manager import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    """Реализация PasswordHasher с использованием bcrypt."""

    def hash_password(self, password: str) -> str:
        """Хеширует пароль."""
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")  # Преобразуем bytes -> str для хранения

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Проверяет пароль."""
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
            return True
        raise InvalidPasswordError
