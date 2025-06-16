from typing import Protocol

from app.domain.entities.specialization import Specialization


class SpecializationReader(Protocol):
    """Интерфейс для чтения специализаций."""

    def get_specializations(self) -> list[Specialization]:
        """Получает информацию о всех специализаций."""
        ...
