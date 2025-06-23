class AdapterError(Exception):
    """Базовый класс для ошибок в слое адаптора."""


class AuthenticationError(AdapterError):
    """Ошибка аутентификации."""
