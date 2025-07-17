from uuid import uuid4

from app.application.interfaces.showcase.showcase_gateway import (
    ShowcaseDeleter,
    ShowcaseReader,
    ShowcaseSaver,
)
from app.application.interfaces.showcase.work_gateway import (
    WorkDeleter,
    WorkReader,
    WorkSaver,
    WorkUpdater,
)
from app.domain.entities.showcase import Showcase, ShowcaseId, Work, WorkId
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


class WorkGateway(
    WorkSaver,
    WorkReader,
    WorkUpdater,
    WorkDeleter,
):
    """Gateway для работы с работами витрины."""

    async def get_work_by_id(self, work_id: WorkId) -> Work:
        """Получает информацию о работе витрины по ID работы."""
        return Work(
            id=work_id,
            showcase_id=ShowcaseId(uuid4()),
            title="fake title",
            description="fake description",
            file_path="fake file_path",
        )

    async def save_work(self, work: Work) -> WorkId:
        """Сохраняет информацию о работе витрины."""
        return work.id

    async def update_work(self, work: Work) -> None:
        """Обновляет обьект работы."""

    async def delete_work(self, work_id: WorkId) -> None:
        """Удаление работы по ID."""
