class DomainError(Exception):
    """Базовая ошибка домена."""


class WeakPasswordError(DomainError):
    """Ошибка, возникающая при слабом пароле."""


class AccessDeniedError(DomainError):
    """Ошибка при запрете доступа."""
