from typing import Protocol

from app.domain.entities.chat import ChatId, ChatMessage, ChatMessageId


class ChatMessageReader(Protocol):
    """Интерфейс для чтения сообщений."""

    async def get_chat_message_by_id(self, message_id: ChatMessageId) -> ChatMessage:
        """Получает сообщение по ID."""
        ...

    async def get_chat_messages_by_chat(self, chat_id: ChatId) -> list[ChatMessage]:
        """Получает сообщения по ID чата."""
        ...


class ChatMessageSaver(Protocol):
    """Интерфейс для сохранения сообщений."""

    async def save_chat_message(self, message: ChatMessage) -> ChatMessageId:
        """Сохраняет сообщение."""
        ...


class ChatMessageDeleter(Protocol):
    """Интерфейс для удаления сообщений."""

    async def delete_chat_message(self, message_id: ChatMessageId) -> None:
        """Удаляет сообщение."""
        ...
