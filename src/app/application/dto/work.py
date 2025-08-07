from dataclasses import dataclass

from app.domain.entities.file_id import FileId
from app.domain.entities.showcase import ShowcaseId, WorkId


@dataclass
class NewWorkDTO:
    """DTO для создания новой работы."""

    title: str
    description: str
    file: bytes


@dataclass
class UpdateWorkDTO:
    """DTO для обновления работы."""

    work_id: WorkId
    title: str | None = None
    description: str | None = None
    file: bytes | None = None


@dataclass
class ReadWorkDTO:
    """DTO для чтения работы."""

    id: WorkId
    showcase_id: ShowcaseId
    title: str
    description: str
    file_path: FileId
