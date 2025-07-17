from typing import Protocol

from app.application.dto.work import UpdateWorkDTO
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.showcase.showcase_gateway import ShowcaseReader
from app.application.interfaces.showcase.work_gateway import WorkReader, WorkUpdater
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.showcase import Work
from app.domain.services.work_service import ensure_can_manage_work
from app.application.interfaces.common.transaction import TransactionManager


class WorkGateway(WorkUpdater, WorkReader, Protocol):
    """Протокол, включающий в себя интерфейсы для обновления и чтения работы витрины."""


class UpdateWorkInteractor:
    """Интерактор для обновления данных работы."""

    def __init__(
        self,
        work_gateway: WorkGateway,
        user_gateway: UserReader,
        showcase_gateway: ShowcaseReader,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
    ) -> None:
        self._work_gateway = work_gateway
        self._user_gateway = user_gateway
        self._showcase_gateway = showcase_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager

    async def __call__(self, data: UpdateWorkDTO) -> None:
        """Обновляет данные пользователя."""
        user_id = self._id_provider()
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        work = await self._work_gateway.get_work_by_id(data.work_id)
        ensure_can_manage_work(showcase, work)
        self.update_work(work, data)
        await self._work_gateway.update_work(work)
        await self._transaction_manager.commit()

    def update_work(
        self,
        work: Work,
        new_data: UpdateWorkDTO,
    ) -> None:
        """Обновляет сущность работы."""
        if new_data.title is not None:
            work.title = new_data.title
        if new_data.description is not None:
            work.description = new_data.description
        if new_data.file_path is not None:
            work.file_path = new_data.file_path
