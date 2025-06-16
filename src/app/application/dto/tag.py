from dataclasses import dataclass

from app.domain.entities.tag import TagId


@dataclass
class TagDTO:
    """DTO для чтения тегов."""

    id: TagId
    name: str
