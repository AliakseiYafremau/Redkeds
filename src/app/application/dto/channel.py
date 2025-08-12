from dataclasses import dataclass

from app.domain.entities.channel import ChannelId


@dataclass
class ChannelDTO:
    """DTO для чтения тегов."""

    id: ChannelId
    name: str
