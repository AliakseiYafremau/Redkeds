from app.application.dto.channel import ChannelDTO
from app.application.interfaces.channel.channel_gateway import ChannelReader


class ReadChannelsInteractor:
    """Интерактор для получения тегов."""

    def __init__(
        self,
        channel_gateway: ChannelReader,
    ) -> None:
        self._channel_gateway = channel_gateway

    async def __call__(self) -> list[ChannelDTO]:
        """Возвращает данные о тегах."""
        channels = await self._channel_gateway.get_channels()
        return [
            ChannelDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in channels
        ]
