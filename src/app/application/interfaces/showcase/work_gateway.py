from typing import Protocol

from app.domain.entities.showcase import Work, WorkId


class WorkReader(Protocol):
    """Интерфейс для чтения данных работы."""

    def get_work_by_id(self, work_id: WorkId) -> None:
        """Получает информацию о работе по ID."""


class WorkSaver(Protocol):
    """Интерфейс для сохранения данных работы."""

    def save_work(self, work: Work) -> None:
        """Сохранение обьект работы."""


class WorkUpdater(Protocol):
    """Интерфейс для обновления данных работы."""

    def update_work(self, work: Work) -> None:
        """Обновления обьекта работы."""


class WorkDeleter(Protocol):
    """Интерфейс для удаления данных работы."""

    def delete_work(self, work_id: WorkId) -> None:
        """Удаление работы по ID."""
