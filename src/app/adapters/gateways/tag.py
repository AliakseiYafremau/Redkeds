from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import TagModel
from app.application.interfaces.tag.tag_gateway import TagReader
from app.domain.entities.tag import Tag


class TagGateway(
    TagReader,
):
    """Gateway для работы с тегами в базе данных."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_tags(self) -> list[Tag]:
        """Получает информацию о всех тегах."""
        result = await self._session.execute(select(TagModel))
        rows = result.fetchall()
        return [Tag(id=row.id, name=row.name) for row in rows]
