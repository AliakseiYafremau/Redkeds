class DomainError(Exception):
    """Базовая ошибка домена."""


class WeakPasswordError(DomainError):
    """Ошибка, возникающая при слабом пароле."""


class CannotCreateShowcaseError(DomainError):
    """Ошибка при создании витрины."""


class CannotUpdateWorkError(DomainError):
    """Ошибка при обновлении работы."""


class CannotManageWorkError(DomainError):
    """Ошибка при управлением состояния работы витрины."""


class CannotManageChatError(DomainError):
    """Ошибка при управлении состояния чата."""


class CannotManageChatMessageError(DomainError):
    """Ошибка при управлении состояни сообщения."""


class CannotManageLikeError(DomainError):
    """Ошибка при управлении лайком."""


class CannotManageSkipError(DomainError):
    """Ошибка при управлении скипом."""
