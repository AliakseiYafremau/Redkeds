from uuid import uuid4

from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
    ShowcaseSaver,
)
from app.domain.entities.showcase import Showcase, ShowcaseId
from app.domain.entities.user_id import UserId


class ShowcaseGateway(
    ShowcaseReader,
    ShowcaseSaver,
    ShowcaseDeleter,
):
    """Gateway для работы с витринами."""

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:  # noqa: ARG002 Так как это фейковая реализация, нам не нужен user_id
        """Получает информацию о витрине по ID пользователя."""
        return Showcase(
            id=ShowcaseId(uuid4()),
        )

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
