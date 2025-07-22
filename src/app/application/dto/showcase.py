from dataclasses import dataclass

from app.application.dto.work import ReadWorkDTO
from app.domain.entities.showcase import ShowcaseId


@dataclass
class ReadShowcaseDTO:
    """DTO для чтения витрины."""

    id: ShowcaseId
    works: list[ReadWorkDTO]
