from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.exceptions import TargetNotFoundError
from redkeds.adapters.mappers import map_model_to_work, map_work_to_model
from redkeds.adapters.models import ShowcaseModel, UserModel, WorkModel
from redkeds.application.interfaces.showcase.showcase_gateway import ShowcaseGateway
from redkeds.application.interfaces.showcase.work_gateway import WorkGateway
from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.showcase import Showcase, ShowcaseId, Work, WorkId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId
from redkeds.domain.entities.user_id import UserId


class SQLShowcaseGateway(ShowcaseGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:
        user_statement = select(UserModel).where(UserModel.id == user_id)
        result = await self._session.execute(user_statement)
        user_model = result.scalar_one_or_none()
        if user_model is None:
            raise TargetNotFoundError(f"User with id {user_id} not found")
        if user_model.showcase_id is None:
            raise TargetNotFoundError(f"User with id {user_id} has no showcase")
        showcase_statement = select(ShowcaseModel).where(
            ShowcaseModel.id == user_model.showcase_id
        )
        result = await self._session.execute(showcase_statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise TargetNotFoundError(
                f"Showcase with id {user_model.showcase_id} not found"
            )
        return Showcase(id=ShowcaseId(showcase_model.id))

    async def save_showcase(self, showcase: Showcase) -> ShowcaseId:
        showcase_model = ShowcaseModel(id=showcase.id)
        self._session.add(showcase_model)
        return showcase.id

    async def get_showcases(
        self,
        exclude_showcase: ShowcaseId | None = None,
        specialization_ids: list[SpecializationId] | None = None,
        city_ids: list[CityId] | None = None,
        tag_ids: list[TagId] | None = None,
        communication_method_ids: list[CommunicationMethodId] | None = None,
    ) -> list[Showcase]:
        """Retrieves all showcases, ignoring exclude_showcase (if specified).

        Sorts showcases by matches with the parameters specialization_ids,
        city_ids, tag_ids, communication_method_ids:
        showcases with matches come first, followed by the rest.
        """
        if exclude_showcase is not None:
            statement = select(ShowcaseModel).where(
                ShowcaseModel.id != exclude_showcase
            )
        else:
            statement = select(ShowcaseModel)
        result = await self._session.execute(statement)
        showcase_models = list(result.scalars().all())

        user_statement = select(UserModel)
        user_result = await self._session.execute(user_statement)
        user_models = user_result.scalars().all()
        showcase_id_to_user = {
            user.showcase_id: user
            for user in user_models
            if user.showcase_id is not None
        }

        def match(user: UserModel | None) -> int:
            score = 0
            if specialization_ids and any(
                spec.id in specialization_ids
                for spec in getattr(user, "specializations", [])
            ):
                score += 1
            if city_ids and user and user.city_id in city_ids:
                score += 1
            if tag_ids and any(tag.id in tag_ids for tag in getattr(user, "tags", [])):
                score += 1
            if (
                communication_method_ids
                and user
                and user.communication_method_id in communication_method_ids
            ):
                score += 1
            return score

        showcase_models.sort(
            key=lambda model: -match(showcase_id_to_user.get(model.id))
            if showcase_id_to_user.get(model.id)
            else 0
        )
        return [Showcase(id=ShowcaseId(model.id)) for model in showcase_models]

    async def update_showcase(self, showcase: Showcase) -> None:
        statement = select(ShowcaseModel).where(ShowcaseModel.id == showcase.id)
        result = await self._session.execute(statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise TargetNotFoundError(f"Showcase with id {showcase.id} not found")
        # Здесь добавьте обновление нужных полей витрины, если они появятся

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        statement = select(ShowcaseModel).where(ShowcaseModel.id == showcase_id)
        result = await self._session.execute(statement)
        showcase_model = result.scalar_one_or_none()
        if showcase_model is None:
            raise TargetNotFoundError(f"Showcase with id {showcase_id} not found")
        await self._session.delete(showcase_model)


class SQLWorkGateway(WorkGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_work_by_id(self, work_id: WorkId) -> Work:
        statement = select(WorkModel).where(WorkModel.id == work_id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise TargetNotFoundError(f"Work with id {work_id} not found")
        return map_model_to_work(work_model)

    async def get_showcase_works_by_id(self, showcase_id: ShowcaseId) -> list[Work]:
        statement = select(WorkModel).where(WorkModel.showcase_id == showcase_id)
        result = await self._session.execute(statement)
        work_models = result.scalars().all()
        return [map_model_to_work(model) for model in work_models]

    async def save_work(self, work: Work) -> WorkId:
        work_model = map_work_to_model(work)
        self._session.add(work_model)
        return work.id

    async def update_work(self, work: Work) -> None:
        statement = select(WorkModel).where(WorkModel.id == work.id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise TargetNotFoundError(f"Work with id {work.id} not found")
        work_model.title = work.title
        work_model.description = work.description
        work_model.file_path = work.file_path
        work_model.showcase_id = work.showcase_id

    async def delete_work(self, work_id: WorkId) -> None:
        statement = select(WorkModel).where(WorkModel.id == work_id)
        result = await self._session.execute(statement)
        work_model = result.scalar_one_or_none()
        if work_model is None:
            raise TargetNotFoundError(f"Work with id {work_id} not found")
        await self._session.delete(work_model)
