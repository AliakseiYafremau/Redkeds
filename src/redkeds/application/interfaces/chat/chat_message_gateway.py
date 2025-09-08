from typing import Protocol

from redkeds.domain.entities.chat import ChatId, ChatMessage, ChatMessageId


class ChatMessageGateway(Protocol):
    async def get_chat_message_by_id(
        self, message_id: ChatMessageId
    ) -> ChatMessage: ...

    async def get_chat_messages_by_chat(self, chat_id: ChatId) -> list[ChatMessage]: ...

    async def save_chat_message(self, message: ChatMessage) -> ChatMessageId: ...

    async def delete_chat_message(self, message_id: ChatMessageId) -> None: ...
