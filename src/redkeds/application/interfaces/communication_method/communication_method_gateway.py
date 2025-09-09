from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.communication_method import CommunicationMethod


class CommunicationMethodGateway(Protocol):
    @abstractmethod
    async def get_communication_methods(self) -> list[CommunicationMethod]:
        raise NotImplementedError
