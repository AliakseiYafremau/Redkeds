from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.showcase import ShowcaseId, Work, WorkId


class WorkGateway(Protocol):
    @abstractmethod
    async def get_work_by_id(self, work_id: WorkId) -> Work:
        raise NotImplementedError

    @abstractmethod
    async def get_showcase_works_by_id(self, showcase_id: ShowcaseId) -> list[Work]:
        raise NotImplementedError

    @abstractmethod
    async def save_work(self, work: Work) -> WorkId:
        raise NotImplementedError

    @abstractmethod
    async def update_work(self, work: Work) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_work(self, work_id: WorkId) -> None:
        raise NotImplementedError
