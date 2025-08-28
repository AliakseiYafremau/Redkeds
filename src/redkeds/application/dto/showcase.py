from dataclasses import dataclass

from redkeds.application.dto.work import ReadWorkDTO
from redkeds.domain.entities.showcase import ShowcaseId


@dataclass
class ReadShowcaseDTO:
    """DTO для чтения витрины."""

    id: ShowcaseId
    works: list[ReadWorkDTO]
