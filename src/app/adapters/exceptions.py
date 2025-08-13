class AdapterError(Exception):
    """Базовый класс для ошибок в слое адаптера."""


class AuthenticationError(AdapterError):
    """Ошибка аутентификации."""


class InvalidPasswordError(AuthenticationError):
    """Неправильный пароль."""


class TargetNotFoundError(AdapterError):
    """Ошибка при не нахождении цели."""


class TargetAlreadyExistError(AdapterError):
    """Ошибка при существовании создаваемой цели."""
