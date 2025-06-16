from dataclasses import dataclass

from app.domain.entities.specialization import SpecializationId


@dataclass
class SpecializationDTO:
    """DTO для чтения специализаций."""

    id: SpecializationId
    name: str
