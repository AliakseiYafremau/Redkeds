from dataclasses import dataclass
from typing import NewType
from uuid import UUID

SpecializationId = NewType("SpecializationId", UUID)


@dataclass
class Specialization:
    """Сущность специализации пользователя.

    Специализация определяет профессиональную область пользователя.
    """

    id: SpecializationId
    name: str
