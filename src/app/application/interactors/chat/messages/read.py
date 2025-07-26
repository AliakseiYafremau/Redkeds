from app.application.dto.chat import ReadChatDTO, ReadChatMessageDTO
from app.application.interfaces.chat.chat_gateway import ChatReader
from app.application.interfaces.chat.chat_message_gateway import ChatMessageReader
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.chat import ChatId
from app.domain.services.chat_service import ensure_can_manage_chat


class ReadMessageInteractor:
    """Интерактор для чтения сообщений."""

    def __init__(
        self,
        id_provider: IdProvider,
        user_gateway: UserReader,
        chat_gateway: ChatReader,
        message_gateway: ChatMessageReader,
    ) -> None:
        self._id_provider = id_provider
        self._user_gateway = user_gateway
        self._chat_gateway = chat_gateway
        self._message_gateway = message_gateway

    async def __call__(self, chat_id: ChatId) -> ReadChatDTO:
        """Отдает сообщения чата."""
        user_id = self._id_provider()
        chat = await self._chat_gateway.get_chat_by_id(chat_id)
        ensure_can_manage_chat(chat, user_id)
        messages = await self._message_gateway.get_chat_messages_by_chat(chat_id)
        messages_dto = [
            ReadChatMessageDTO(
                id=message.id,
                chat_id=message.chat_id,
                sender_id=message.sender_id,
                text=message.text,
                timestamp=message.timestamp,
            )
            for message in messages
        ]
        return ReadChatDTO(
            id=chat.id,
            user1_id=chat.user1_id,
            user2_id=chat.user2_id,
            messages=messages_dto,
        )
