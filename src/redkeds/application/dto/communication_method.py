from dataclasses import dataclass

from redkeds.domain.entities.communication_method import CommunicationMethodId


@dataclass
class CommunicationMethodDTO:
    """DTO для получения способов общения."""

    id: CommunicationMethodId | None
    name: str
