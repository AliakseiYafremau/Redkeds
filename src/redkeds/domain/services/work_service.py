from redkeds.domain.entities.showcase import Showcase, Work
from redkeds.domain.exceptions import AccessDeniedError


def ensure_can_manage_work(showcase: Showcase, work: Work) -> bool:
    """Проверяет возможность управление работой витрины."""
    if showcase.id != work.showcase_id:
        raise AccessDeniedError("Нет доступа к изменении работы витрины.")
    return True
