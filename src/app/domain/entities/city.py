from dataclasses import dataclass
from typing import NewType
from uuid import UUID

CityId = NewType("CityId", UUID)


@dataclass
class City:
    """Сущность города."""

    id: CityId
    name: str
