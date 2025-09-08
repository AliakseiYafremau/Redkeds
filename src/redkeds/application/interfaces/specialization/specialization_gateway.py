from typing import Protocol

from redkeds.domain.entities.specialization import Specialization


class SpecializationGateway(Protocol):
    async def get_specializations(self) -> list[Specialization]: ...
