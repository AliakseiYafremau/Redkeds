from dataclasses import dataclass

from app.domain.entities.showcase import ShowcaseId


@dataclass
class NewSkipDTO:
    """DTO для добавления скипа."""

    showcase_id: ShowcaseId
