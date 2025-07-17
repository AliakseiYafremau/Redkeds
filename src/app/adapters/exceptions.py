class AdapterError(Exception):
    """Базовый класс для ошибок в слое адаптера."""


class AuthenticationError(AdapterError):
    """Ошибка аутентификации."""


class InvalidPasswordError(AuthenticationError):
    """Неправильный пароль."""


class UserAlreadyExistsError(AdapterError):
    """Ошибка при попытке создания уже существующего пользователя."""


class UserDoesNotExistError(AdapterError):
    """Ошибка при попытке получить несуществующего пользователя."""


class TagDoesNotExistError(AdapterError):
    """Ошибка при обращении к несуществуещему тегу."""


class SpecializationDoesNotExistError(AdapterError):
    """Ошибка при обращении к несуществующей специальности."""


class CommunicationMethodDoesNotExistError(AdapterError):
    """Ошибка при обращении к несуществющему методу связи."""


class WorkDoesNotExistError(AdapterError):
    """Ошибка при попытке получить несуществующую работу."""
