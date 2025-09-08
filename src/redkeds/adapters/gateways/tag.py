from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import TagModel
from redkeds.application.interfaces.tag.tag_gateway import TagGateway
from redkeds.domain.entities.tag import Tag, TagId


class SQLTagGateway(TagGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_tags(self) -> list[Tag]:
        result = await self._session.execute(select(TagModel))
        rows = result.scalars().all()
        return [Tag(id=TagId(row.id), name=row.name) for row in rows]
