from dataclasses import dataclass

from app.domain.entities.showcase import ShowcaseId, WorkId


@dataclass
class NewWorkDTO:
    """DTO для создания новой работы."""

    title: str
    description: str
    file_path: str


@dataclass
class UpdateWorkDTO:
    """DTO для обновления работы."""

    work_id: WorkId
    title: str | None
    description: str | None
    file_path: str | None


@dataclass
class ReadWorkDTO:
    """DTO для чтения работы."""

    showcase_id: ShowcaseId
    title: str
    description: str
    file_path: str
