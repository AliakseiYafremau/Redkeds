from app.domain.entities.showcase import Showcase, Work
from app.domain.exceptions import CannotManageWorkError


def ensure_can_manage_work(showcase: Showcase, work: Work) -> bool:
    """Проверяет возможность управление обьектом."""
    if showcase.id != work.showcase_id:
        raise CannotManageWorkError
    return True
