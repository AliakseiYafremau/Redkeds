from typing import Protocol

from app.domain.entities.skip import Skip, SkipId


class SkipSaver(Protocol):
    """Интерфейс для добавления скипов."""

    async def add_skip(self, skip: Skip) -> SkipId:
        """Добволяет скип витрине от пользователя."""
        ...


class SkipDeleter(Protocol):
    """Интерфейс для удаления скипов."""

    async def delete_skip(self, skip_id: SkipId) -> None:
        """Удаляет скип витрины от пользователя."""
        ...


class SkipReader(Protocol):
    """Интерфейс для получения скипа."""

    async def get_skip_by_id(self, skip_id: SkipId) -> Skip:
        """Получает скип по ID."""
        ...
