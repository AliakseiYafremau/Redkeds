from app.application.interfaces.specialization.specialization_gateway import (
    SpecializationReader,
)
from app.domain.entities.specialization import Specialization


class SpecializationGateway(
    SpecializationReader,
):
    """Gateway для работы со специализациями пользователя."""

    async def get_specializations(self) -> list[Specialization]:
        """Получает список о всех специализациях."""
        return []
