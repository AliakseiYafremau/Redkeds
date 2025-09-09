from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.specialization import Specialization


class SpecializationGateway(Protocol):
    @abstractmethod
    async def get_specializations(self) -> list[Specialization]:
        raise NotImplementedError
