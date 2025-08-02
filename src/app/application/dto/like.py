from dataclasses import dataclass

from app.domain.entities.user_id import UserId
from app.domain.entities.showcase import ShowcaseId


@dataclass
class LikeDTO:
    user_id: UserId
    showcase_id: ShowcaseId
