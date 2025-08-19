from dataclasses import dataclass

from app.domain.entities.showcase import ShowcaseId


@dataclass
class NewLikeDTO:
    """DTO для добавления лайка."""

    showcase_id: ShowcaseId
