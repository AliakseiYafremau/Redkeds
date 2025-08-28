from typing import Protocol

from redkeds.domain.entities.specialization import Specialization


class SpecializationReader(Protocol):
    """Интерфейс для чтения специализаций."""

    async def get_specializations(self) -> list[Specialization]:
        """Получает информацию о всех специализаций."""
        ...
