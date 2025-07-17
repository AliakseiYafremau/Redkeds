from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.exceptions import WorkDoesNotExistError
from app.adapters.mappers import map_model_to_work, map_work_to_model
from app.adapters.models import WorkModel
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

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_work_by_id(self, work_id: WorkId) -> Work:
        """Получает информацию о работе витрины по ID работы."""
        statement = select(WorkModel).where(WorkModel.id == work_id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise WorkDoesNotExistError(f"Work with id {work_id} not found")
        return map_model_to_work(work_model)

    async def save_work(self, work: Work) -> WorkId:
        """Сохраняет информацию о работе витрины."""
        work_model = map_work_to_model(work)
        self._session.add(work_model)
        return work.id

    async def update_work(self, work: Work) -> None:
        """Обновляет обьект работы."""
        statement = select(WorkModel).where(WorkModel.id == work.id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise WorkDoesNotExistError(f"Work with id {work.id} not found")
        work_model.title = work.title
        work_model.description = work.description
        work_model.file_path = work.file_path
        work_model.showcase_id = work.showcase_id

    async def delete_work(self, work_id: WorkId) -> None:
        """Удаление работы по ID."""
        statement = select(WorkModel).where(WorkModel.id == work_id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise WorkDoesNotExistError(f"Work with id {work_id} not found")
        await self._session.delete(work_model)
