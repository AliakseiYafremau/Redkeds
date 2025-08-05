from app.application.dto.showcase import ReadShowcaseDTO
from app.application.dto.work import ReadWorkDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.showcase.showcase_gateway import ShowcaseReader
from app.application.interfaces.showcase.work_gateway import WorkReader
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.showcase import WorkId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.logs import get_logger

logger = get_logger(__name__)


class ReadRecommendationFeed:
    """Интерактор для получения ленты рекомендаций."""

    def __init__(
        self,
        id_provider: IdProvider,
        showcase_gateway: ShowcaseReader,
        work_gateway: WorkReader,
    ) -> None:
        self._id_provider = id_provider
        self._showcase_gateway = showcase_gateway
        self._work_gateway = work_gateway

    async def __call__(
        self,
        specialization_ids: list[SpecializationId] | None = None,
        city_ids: list[CityId] | None = None,
        tag_ids: list[TagId] | None = None,
        communication_method_ids: list[CommunicationMethodId] | None = None,
    ) -> list[ReadShowcaseDTO]:
        """Получает ленту рекомендаций."""
        user_id = self._id_provider()
        user_showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        showcases = await self._showcase_gateway.get_showcases(
            exclude_showcase=user_showcase.id,
            specialization_ids=specialization_ids,
            city_ids=city_ids,
            tag_ids=tag_ids,
            communication_method_ids=communication_method_ids,
        )
        showcases_dto: list[ReadShowcaseDTO] = []
        for showcase in showcases:
            works = await self._work_gateway.get_showcase_works_by_id(showcase.id)
            work_dto_list: list[ReadWorkDTO] = [
                ReadWorkDTO(
                    id=WorkId(work.id),
                    showcase_id=work.showcase_id,
                    title=work.title,
                    description=work.description,
                    file_path=work.file_path,
                )
                for work in works
            ]
            showcases_dto.append(ReadShowcaseDTO(id=showcase.id, works=work_dto_list))
        return showcases_dto
