from typing import Protocol

from app.domain.entities.showcase import Showcase


class ShowcaseSaver(Protocol):
    """Интерфейс для сохранения витрины."""

    def save_showcase(self, showcase: Showcase) -> None:
        """Сохраняет обьект витрины."""
        ...
