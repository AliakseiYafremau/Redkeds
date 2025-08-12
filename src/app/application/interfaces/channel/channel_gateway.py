from typing import Protocol

from app.domain.entities.channel import Channel


class ChannelReader(Protocol):
    """Интерфейс для получения методов общения."""

    async def get_channels(self) -> list[Channel]:
        """Получает все методы общения."""
        ...
