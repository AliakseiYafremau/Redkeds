from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseSaver,
)
from app.domain.entities.showcase import Showcase, ShowcaseId


class ShowcaseGateway(
    ShowcaseSaver,
    ShowcaseDeleter,
):
    """Gateway для работы с витринами."""

    async def save_showcase(self, showcase: Showcase) -> None:
        """Сохраняет обьект витрины."""

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
