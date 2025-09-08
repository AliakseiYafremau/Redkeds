from redkeds.application.dto.specialization import SpecializationDTO
from redkeds.application.interfaces.specialization.specialization_gateway import (
    SpecializationGateway,
)


class ReadSpecializationsInteractor:
    """Интерактор для получения специализаций."""

    def __init__(
        self,
        specialization_gateway: SpecializationGateway,
    ) -> None:
        self._specialization_gateway = specialization_gateway

    async def __call__(self) -> list[SpecializationDTO]:
        """Возвращает данные о специализациях."""
        specializations = await self._specialization_gateway.get_specializations()
        return [
            SpecializationDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in specializations
        ]
