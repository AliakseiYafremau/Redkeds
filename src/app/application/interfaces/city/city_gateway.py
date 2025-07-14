from typing import Protocol

from app.domain.entities.city import City


class CityReader(Protocol):
    """Интерфейс для чтения городов."""

    async def get_cities(self) -> list[City]:
        """Получает информацию о всех городах."""
        ...
