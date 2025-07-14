from dataclasses import dataclass

from app.domain.entities.city import CityId


@dataclass
class CityDTO:
    """DTO для чтения специализаций."""

    id: CityId
    name: str
