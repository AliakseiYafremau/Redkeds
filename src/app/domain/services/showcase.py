from app.domain.entities.user import User
from app.domain.exceptions import CannotCreateShowcaseError


def ensure_can_create_showcase(user: User) -> bool:
    """Проверяет можно ли создать витрину для пользователя.

    Пользователь может иметь только одну витрину.
    """
    if user.specialization is not None:
        raise CannotCreateShowcaseError

    return True
