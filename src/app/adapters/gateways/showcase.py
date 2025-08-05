from sqlalchemy import select, join
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.exceptions import ShowcaseDoesNotExistError, WorkDoesNotExistError
from app.adapters.mappers import map_model_to_work, map_work_to_model
from app.adapters.models import ShowcaseModel, UserModel, WorkModel
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

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:
        """Получает информацию о витрине по ID пользователя."""
        user_statement = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(user_statement)
        user_model = result.scalar_one_or_none()
        if user_model is None:
            raise ShowcaseDoesNotExistError(f"User with id {user_id} not found")
        if user_model.showcase_id is None:
            raise ShowcaseDoesNotExistError(f"User with id {user_id} has no showcase")
        showcase_statement = select(ShowcaseModel).where(
            ShowcaseModel.id == user_model.showcase_id
        )
        result = await self._session.execute(showcase_statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise ShowcaseDoesNotExistError(
                f"Showcase with id {user_model.showcase_id} not found"
            )
        return Showcase(id=ShowcaseId(showcase_model.id))

    async def save_showcase(self, showcase: Showcase) -> ShowcaseId:
        """Сохраняет витрину в базе данных."""
        showcase_model = ShowcaseModel(id=showcase.id)
        self._session.add(showcase_model)
        return showcase.id

    async def get_showcases(
        self,
        exclude_showcase: ShowcaseId | None = None,
    ) -> list[Showcase]:
        """Возвращает все витрины, отсортированные по пользователю (user_id).

        Если exclude_showcase задан, исключает его из результата.
        """
        j = join(ShowcaseModel, UserModel, ShowcaseModel.id == UserModel.showcase_id)
        if exclude_showcase is not None:
            statement = (
                select(ShowcaseModel)
                .select_from(j)
                .where(ShowcaseModel.id != exclude_showcase)
                .order_by(UserModel.id)
            )
        else:
            statement = (
                select(ShowcaseModel)
                .select_from(j)
                .order_by(UserModel.id)
            )
        result = await self._session.execute(statement)
        showcase_models = result.scalars().all()
        return [Showcase(id=ShowcaseId(model.id)) for model in showcase_models]

    async def update_showcase(self, showcase: Showcase) -> None:
        """Обновляет данные витрины."""
        statement = select(ShowcaseModel).where(ShowcaseModel.id == showcase.id)
        result = await self._session.execute(statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise ShowcaseDoesNotExistError(f"Showcase with id {showcase.id} not found")
        # Здесь добавьте обновление нужных полей витрины, если они появятся

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
        statement = select(ShowcaseModel).where(ShowcaseModel.id == showcase_id)
        result = await self._session.execute(statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise ShowcaseDoesNotExistError(f"Showcase with id {showcase_id} not found")
        await self._session.delete(showcase_model)


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

    async def get_showcase_works_by_id(self, showcase_id: ShowcaseId) -> list[Work]:
        """Получает информацию о всех работах витрины по ID."""
        statement = select(WorkModel).where(WorkModel.showcase_id == showcase_id)
        result = await self._session.execute(statement)
        work_models = result.scalars().all()
        return [map_model_to_work(model) for model in work_models]

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
