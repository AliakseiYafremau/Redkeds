from app.application.dto.specialization import SpecializationDTO
from app.application.interfaces.specialization.specialization_gateway import (
    SpecializationReader,
)


class ReadSpecializationsInteractor:
    """Интерактор для получения специализаций."""

    def __init__(
        self,
        specialization_gateway: SpecializationReader,
    ) -> None:
        self._specialization_gateway = specialization_gateway

    def __call__(self) -> list[SpecializationDTO]:
        """Возвращает данные о специализациях."""
        specializations = self._specialization_gateway.get_specializations()
        return [
            SpecializationDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in specializations
        ]
