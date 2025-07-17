from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import CityModel
from app.application.interfaces.city.city_gateway import CityReader
from app.domain.entities.city import City, CityId


class CityGateway(
    CityReader,
):
    """Gateway для работы с городами в базе данных."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_cities(self) -> list[City]:
        """Получает информацию о всех городах."""
        result = await self._session.execute(select(CityModel))
        rows = result.scalars().all()
        return [City(id=CityId(row.id), name=row.name) for row in rows]
