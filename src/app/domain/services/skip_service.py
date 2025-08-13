from app.domain.entities.skip import Skip
from app.domain.entities.user_id import UserId
from app.domain.exceptions import AccessDeniedError


def ensure_can_manage_skip(skip: Skip, user_id: UserId) -> bool:
    """Проверяет возможность управление скипом."""
    if skip.user_id != user_id:
        raise AccessDeniedError("Нет доступа к скипу.")
    return True
