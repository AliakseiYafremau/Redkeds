from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import CityModel
from redkeds.application.interfaces.city.city_gateway import CityGateway
from redkeds.domain.entities.city import City, CityId


class SQLCityGateway(CityGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_cities(self) -> list[City]:
        result = await self._session.execute(select(CityModel))
        rows = result.scalars().all()
        return [City(id=CityId(row.id), name=row.name) for row in rows]
