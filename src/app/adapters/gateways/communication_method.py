from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import CommunicationMethodModel
from app.application.interfaces.communication_method.communication_method_gateway import (  # noqa: E501
    CommunicationMethodReader,
)
from app.domain.entities.communication_method import (
    CommunicationMethod,
    CommunicationMethodId,
)


class CommunicationMethodGateway(
    CommunicationMethodReader,
):
    """Gateway для работы со способами общения в базе данных."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_communication_methods(self) -> list[CommunicationMethod]:
        """Получает информацию о всех способах общения."""
        result = await self._session.execute(select(CommunicationMethodModel))
        rows = result.scalars().all()
        return [
            CommunicationMethod(id=CommunicationMethodId(row.id), name=row.name)
            for row in rows
        ]
