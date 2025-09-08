from redkeds.application.dto.chat import ReadShortChatDTO
from redkeds.application.interfaces.chat.chat_gateway import ChatGateway
from redkeds.application.interfaces.common.id_provider import IdProvider


class ReadUserChatInteractor:
    """Интерактор для получения всех чатов пользователя."""

    def __init__(
        self,
        chat_gateway: ChatGateway,
        id_provider: IdProvider,
    ) -> None:
        self._chat_gateway = chat_gateway
        self._id_provider = id_provider

    async def __call__(self) -> list[ReadShortChatDTO]:
        """Возвращение всех чатов пользователя."""
        user_id = self._id_provider()
        chats = await self._chat_gateway.get_user_chats(user_id)
        return [
            ReadShortChatDTO(
                id=chat.id,
                user1_id=chat.user1_id,
                user2_id=chat.user2_id,
            )
            for chat in chats
        ]
