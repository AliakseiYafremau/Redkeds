from dataclasses import dataclass

from redkeds.domain.entities.specialization import SpecializationId


@dataclass
class SpecializationDTO:
    """DTO для чтения специализаций."""

    id: SpecializationId
    name: str
