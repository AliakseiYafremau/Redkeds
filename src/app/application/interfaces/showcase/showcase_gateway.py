from typing import Protocol

from app.domain.entities.showcase import Showcase, ShowcaseId
from app.domain.entities.user_id import UserId


class ShowcaseReader(Protocol):
    """Интерфейс для чтения данных витрины."""

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:
        """Получает информацию о витрине по ID пользователя."""
        ...

    async def get_showcases(
        self, exclude_showcase: ShowcaseId | None = None
    ) -> list[Showcase]:
        """Получает все витрины, игнорируя exclude_showcase."""
        ...


class ShowcaseSaver(Protocol):
    """Интерфейс для сохранения витрины."""

    async def save_showcase(self, showcase: Showcase) -> ShowcaseId:
        """Сохраняет обьект витрины."""
        ...


class ShowcaseDeleter(Protocol):
    """Интерфейс для удаления витрины."""

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
        ...
