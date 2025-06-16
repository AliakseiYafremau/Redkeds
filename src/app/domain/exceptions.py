class DomainError(Exception):
    """Базовая ошибка домена."""


class WeakPasswordError(DomainError):
    """Ошибка, возникающая при слабом пароле."""


class CannotCreateShowcaseError(DomainError):
    """Ошибка при создании витрины."""
