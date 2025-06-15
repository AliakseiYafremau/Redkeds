from dataclasses import dataclass
from typing import NewType

SpecializationId = NewType("SpecializationId", int)


@dataclass
class Specialization:
    """Сущность специализации пользователя.

    Специализация определяет профессиональную область пользователя.
    """

    id: SpecializationId | None
    name: str
