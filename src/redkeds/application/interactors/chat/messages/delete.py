from typing import Protocol

from redkeds.application.interfaces.chat.chat_gateway import ChatReader
from redkeds.application.interfaces.chat.chat_message_gateway import (
    ChatMessageDeleter,
    ChatMessageReader,
)
from redkeds.application.interfaces.common.id_provider import IdProvider
from redkeds.domain.entities.chat import ChatMessageId
from redkeds.domain.services.chat_service import (
    ensure_can_manage_chat,
    ensure_can_manage_chat_message,
)


class ChatMessageGateway(ChatMessageDeleter, ChatMessageReader, Protocol):
    """Интерфейс удаления и чтения сообщения."""


class DeleteChatMessageInteractor:
    """Интерактор для удаления сообщения."""

    def __init__(
        self,
        id_provider: IdProvider,
        chat_gateway: ChatReader,
        message_gateway: ChatMessageGateway,
    ) -> None:
        self._id_provider = id_provider
        self._chat_gateway = chat_gateway
        self._message_gateway = message_gateway

    async def __call__(self, message_id: ChatMessageId) -> None:
        """Удаляет сообщение."""
        user_id = self._id_provider()
        message = await self._message_gateway.get_chat_message_by_id(message_id)
        chat = await self._chat_gateway.get_chat_by_id(message.chat_id)
        ensure_can_manage_chat(chat, user_id)
        ensure_can_manage_chat_message(message, user_id)
        await self._message_gateway.delete_chat_message(message_id)
