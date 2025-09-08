from redkeds.application.dto.communication_method import CommunicationMethodDTO
from redkeds.application.interfaces.communication_method.communication_method_gateway import (  # noqa: E501
    CommunicationMethodGateway,
)


class ReadCommunicationMethodsInteractor:
    """Интерактор для получения способов общения."""

    def __init__(
        self,
        communication_method_gateway: CommunicationMethodGateway,
    ) -> None:
        self._communication_method_gateway = communication_method_gateway

    async def __call__(self) -> list[CommunicationMethodDTO]:
        """Возвращает данные о способах общения."""
        communication_methods = (
            await self._communication_method_gateway.get_communication_methods()
        )
        return [
            CommunicationMethodDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in communication_methods
        ]
