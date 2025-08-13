from app.domain.entities.like import Like
from app.domain.entities.user_id import UserId
from app.domain.exceptions import AccessDeniedError


def ensure_can_manage_like(like: Like, user_id: UserId) -> bool:
    """Проверяет возможность управление лайком."""
    if like.user_id != user_id:
        raise AccessDeniedError("Нет доступа к лайкам.")
    return True
