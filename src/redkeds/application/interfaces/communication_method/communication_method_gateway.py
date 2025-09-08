from typing import Protocol

from redkeds.domain.entities.communication_method import CommunicationMethod


class CommunicationMethodGateway(Protocol):
    async def get_communication_methods(self) -> list[CommunicationMethod]: ...
