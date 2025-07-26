from typing import Protocol

from app.application.interfaces.chat.chat_gateway import ChatDeleter, ChatReader
from app.application.interfaces.common.id_provider import IdProvider
from app.domain.entities.chat import ChatId
from app.domain.services.chat_service import ensure_can_manage_chat


class ChatGateway(ChatDeleter, ChatReader, Protocol):
    """Интерфейс для удаления и чтения чата."""


class DeleteChatInteractor:
    """Интерфейс для удаления чата."""

    def __init__(
        self,
        chat_gateway: ChatGateway,
        id_provider: IdProvider,
    ) -> None:
        self._chat_gateway = chat_gateway
        self._id_provider = id_provider

    async def __call__(self, chat_id: ChatId) -> None:
        """Удаляет чат."""
        user_id = self._id_provider()
        chat = await self._chat_gateway.get_chat_by_id(chat_id)
        ensure_can_manage_chat(chat, user_id)
        await self._chat_gateway.delete_chat(chat_id)
