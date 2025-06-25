from typing import Protocol

from app.domain.entities.user_id import UserId
from app.domain.entities.showcase import Showcase, ShowcaseId


class ShowcaseReader(Protocol):
    """Интерфейс для чтения данных витрины."""

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:
        """Получает информацию о витрине по ID пользователя."""
        ...

class ShowcaseSaver(Protocol):
    """Интерфейс для сохранения витрины."""

    async def save_showcase(self, showcase: Showcase) -> None:
        """Сохраняет обьект витрины."""
        ...


class ShowcaseDeleter(Protocol):
    """Интерфейс для удаления витрины."""

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
        ...

