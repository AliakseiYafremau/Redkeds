from typing import Protocol

from app.domain.entities.showcase import Showcase, ShowcaseId


class ShowcaseSaver(Protocol):
    """Интерфейс для сохранения витрины."""

    def save_showcase(self, showcase: Showcase) -> None:
        """Сохраняет обьект витрины."""
        ...


class ShowcaseDeleter(Protocol):
    """Интерфейс для удаления витрины."""

    def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
        ...
