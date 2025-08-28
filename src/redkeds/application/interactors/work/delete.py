from typing import Protocol

from redkeds.application.interfaces.common.file_gateway import FileManager
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.application.interfaces.common.transaction import TransactionManager
from redkeds.application.interfaces.showcase.showcase_gateway import ShowcaseReader
from redkeds.application.interfaces.showcase.work_gateway import WorkDeleter, WorkReader
from redkeds.domain.entities.showcase import WorkId
from redkeds.domain.services.work_service import ensure_can_manage_work


class WorkGateway(WorkReader, WorkDeleter, Protocol):
    """Протокол, включающий в себя интерфейсы для удаления и чтения работы."""


class DeleteWorkInteractor:
    """Интерактор для удаления работы витрины."""

    def __init__(
        self,
        work_gateway: WorkGateway,
        showcase_gateway: ShowcaseReader,
        id_provider: IdProvider,
        transaction_manager: TransactionManager,
        file_manager: FileManager,
    ) -> None:
        self._work_gateway = work_gateway
        self._showcase_gateway = showcase_gateway
        self._id_provider = id_provider
        self._transaction_manager = transaction_manager
        self._file_manager = file_manager

    async def __call__(self, work_id: WorkId) -> None:
        """Удаляет данные работы витрины."""
        user_id = self._id_provider()
        showcase = await self._showcase_gateway.get_showcase_by_user_id(user_id)
        work = await self._work_gateway.get_work_by_id(work_id)
        ensure_can_manage_work(showcase, work)
        await self._work_gateway.delete_work(work_id)
        await self._file_manager.delete(work.file_path)
        await self._transaction_manager.commit()
