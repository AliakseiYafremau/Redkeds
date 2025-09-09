from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.city import City


class CityGateway(Protocol):
    @abstractmethod
    async def get_cities(self) -> list[City]:
        raise NotImplementedError
