from app.application.dto.work import NewWorkDTO
from app.application.interfaces.common.file_gateway import FileManager
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.showcase.showcase_gateway import ShowcaseReader
from app.application.interfaces.showcase.work_gateway import (
    WorkSaver,
)
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.showcase import Work, WorkId


class CreateWorkInteractor:
    """Интерактор для добавления работы."""

    def __init__(
        self,
        work_gateway: WorkSaver,
        user_gateway: UserReader,
        id_provider: IdProvider,
        showcase_gateway: ShowcaseReader,
        uuid_generator: UUIDGenerator,
        transaction_manager: TransactionManager,
        file_manager: FileManager,
    ) -> None:
        self._work_gateway = work_gateway
        self._user_gateway = user_gateway
        self._id_provider = id_provider
        self._showcase_gateway = showcase_gateway
        self._uuid_generator = uuid_generator
        self._transtaction_manager = transaction_manager
        self._file_manager = file_manager

    async def __call__(self, data: NewWorkDTO) -> WorkId:
        """Добавляет работу в витрину пользователя."""
        user_id = self._id_provider()
        work_id = WorkId(self._uuid_generator())
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        file_id = await self._file_manager.save(data.file)
        work = Work(
            id=work_id,
            showcase_id=showcase.id,
            title=data.title,
            description=data.description,
            file_path=file_id,
        )
        await self._work_gateway.save_work(work)
        await self._transtaction_manager.commit()
        return work_id
