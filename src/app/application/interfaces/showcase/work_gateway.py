from typing import Protocol

from app.domain.entities.showcase import ShowcaseId, Work, WorkId


class WorkReader(Protocol):
    """Интерфейс для чтения данных работы."""

    async def get_work_by_id(self, work_id: WorkId) -> Work:
        """Получает информацию о работе по ID."""
        ...

    async def get_showcase_works_by_id(self, showcase_id: ShowcaseId) -> list[Work]:
        """Получает все работы витрины по ее ID."""
        ...


class WorkSaver(Protocol):
    """Интерфейс для сохранения данных работы."""

    async def save_work(self, work: Work) -> WorkId:
        """Сохранение обьект работы."""
        ...


class WorkUpdater(Protocol):
    """Интерфейс для обновления данных работы."""

    async def update_work(self, work: Work) -> None:
        """Обновление обьекта работы."""
        ...


class WorkDeleter(Protocol):
    """Интерфейс для удаления данных работы."""

    async def delete_work(self, work_id: WorkId) -> None:
        """Удаление работы по ID."""
        ...
