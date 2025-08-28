from dataclasses import dataclass

from redkeds.domain.entities.city import CityId


@dataclass
class CityDTO:
    """DTO для чтения специализаций."""

    id: CityId
    name: str
