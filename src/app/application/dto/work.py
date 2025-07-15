from dataclasses import dataclass


@dataclass
class NewWorkDTO:
    """DTO для создания новой работы."""

    title: str
    description: str
    file_path: str
