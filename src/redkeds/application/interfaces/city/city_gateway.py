from typing import Protocol

from redkeds.domain.entities.city import City


class CityGateway(Protocol):
    async def get_cities(self) -> list[City]: ...
