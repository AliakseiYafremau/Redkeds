from dataclasses import dataclass

from app.domain.entities.communication_method import CommunicationMethodId


@dataclass
class CommunicationMethodDTO:
    """DTO для получения способов общения."""

    id: CommunicationMethodId | None
    name: str
