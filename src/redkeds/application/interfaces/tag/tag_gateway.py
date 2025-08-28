from typing import Protocol

from redkeds.domain.entities.tag import Tag


class TagReader(Protocol):
    """Интерфейс для чтения тегов."""

    async def get_tags(self) -> list[Tag]:
        """Получает информацию о всех тегах."""
        ...
