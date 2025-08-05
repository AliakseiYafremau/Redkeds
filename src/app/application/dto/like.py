from dataclasses import dataclass

from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.user_id import UserId


@dataclass
class NewLikeDTO:
    """DTO для добавления лайка."""

    user_id: UserId
    showcase_id: ShowcaseId
