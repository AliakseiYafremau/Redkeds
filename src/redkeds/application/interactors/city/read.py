from redkeds.application.dto.city import CityDTO
from redkeds.application.interfaces.city.city_gateway import (
    CityGateway,
)


class ReadCitiesInteractor:
    """Интерактор для получения городов."""

    def __init__(
        self,
        city_gateway: CityGateway,
    ) -> None:
        self._city_gateway = city_gateway

    async def __call__(self) -> list[CityDTO]:
        """Возвращает данные о городов."""
        cities = await self._city_gateway.get_cities()
        return [
            CityDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in cities
        ]
