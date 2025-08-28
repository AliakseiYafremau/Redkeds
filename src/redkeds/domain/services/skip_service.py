from redkeds.domain.entities.skip import Skip
from redkeds.domain.entities.user_id import UserId
from redkeds.domain.exceptions import AccessDeniedError


def ensure_can_manage_skip(skip: Skip, user_id: UserId) -> bool:
    """Проверяет возможность управление скипом."""
    if str(skip.user_id) != str(user_id):
        raise AccessDeniedError("Нет доступа к скипу.")
    return True
