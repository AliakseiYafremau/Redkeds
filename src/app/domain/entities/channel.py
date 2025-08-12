from dataclasses import dataclass
from typing import NewType
from uuid import UUID

ChannelId = NewType("ChannelId", UUID)


@dataclass
class Channel:
    """Методы общения."""

    id: ChannelId
    name: str
