from typing import Protocol

from redkeds.domain.entities.communication_method import CommunicationMethod


class CommunicationMethodReader(Protocol):
    """Интерфейс для получения методов общения."""

    async def get_communication_methods(self) -> list[CommunicationMethod]:
        """Получает все методы общения."""
        ...
