from app.application.dto.work import ReadWorkDTO
from app.application.interfaces.showcase.work_gateway import WorkReader
from app.domain.entities.showcase import ShowcaseId, WorkId


class ReadWorkInteractor:
    """Интерактор для чтения данных работы."""

    def __init__(
        self,
        work_gateway: WorkReader,
    ) -> None:
        self._work_gateway = work_gateway

    async def __call__(self, work_id: WorkId) -> ReadWorkDTO:
        """Читает данные о работе витрины пользователя."""
        work = await self._work_gateway.get_work_by_id(work_id)
        return ReadWorkDTO(
            id=work_id,
            showcase_id=work.showcase_id,
            title=work.title,
            description=work.description,
            file_path=work.file_path,
        )


class ReadAllWorksInteractor:
    """Интерактор для получения информациио всех работах витрины."""

    def __init__(
        self,
        work_gateway: WorkReader,
    ) -> None:
        self._work_gateway = work_gateway

    async def __call__(self, showcase_id: ShowcaseId) -> list[ReadWorkDTO]:
        """Возвращает данные о работах по ID витрины."""
        return [
            ReadWorkDTO(
                id=work.id,
                showcase_id=work.showcase_id,
                title=work.title,
                description=work.description,
                file_path=work.file_path,
            )
            for work in await self._work_gateway.get_showcase_works_by_id(showcase_id)
        ]
