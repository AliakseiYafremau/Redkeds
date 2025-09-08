from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import SpecializationModel
from redkeds.application.interfaces.specialization.specialization_gateway import (
    SpecializationGateway,
)
from redkeds.domain.entities.specialization import Specialization, SpecializationId


class SQLSpecializationGateway(SpecializationGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_specializations(self) -> list[Specialization]:
        result = await self._session.execute(select(SpecializationModel))
        rows = result.scalars().all()
        return [
            Specialization(id=SpecializationId(row.id), name=row.name) for row in rows
        ]
