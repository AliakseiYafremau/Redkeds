from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import SpecializationModel
from app.application.interfaces.specialization.specialization_gateway import (
    SpecializationReader,
)
from app.domain.entities.specialization import Specialization, SpecializationId


class SpecializationGateway(
    SpecializationReader,
):
    """Gateway для работы со специализациями пользователя."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_specializations(self) -> list[Specialization]:
        """Получает список о всех специализациях."""
        result = await self._session.execute(select(SpecializationModel))
        rows = result.scalars().all()
        return [
            Specialization(id=SpecializationId(row.id), name=row.name) for row in rows
        ]
