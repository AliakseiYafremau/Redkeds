from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.models import ChannelModel
from app.application.interfaces.channel.channel_gateway import ChannelReader
from app.domain.entities.channel import Channel, ChannelId


class ChannelGateway(
    ChannelReader,
):
    """Gateway для работы с тегами в базе данных."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_channels(self) -> list[Channel]:
        """Получает информацию о всех тегах."""
        result = await self._session.execute(select(ChannelModel))
        rows = result.scalars().all()
        return [Channel(id=ChannelId(row.id), name=row.name) for row in rows]
