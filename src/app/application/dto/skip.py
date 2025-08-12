from dataclasses import dataclass

from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.user_id import UserId


@dataclass
class NewSkipDTO:
    """DTO для добавления скипа."""

    user_id: UserId
    showcase_id: ShowcaseId
