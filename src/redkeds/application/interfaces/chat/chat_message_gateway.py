from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.chat import ChatId, ChatMessage, ChatMessageId


class ChatMessageGateway(Protocol):
    @abstractmethod
    async def get_chat_message_by_id(self, message_id: ChatMessageId) -> ChatMessage:
        raise NotImplementedError

    @abstractmethod
    async def get_chat_messages_by_chat(self, chat_id: ChatId) -> list[ChatMessage]:
        raise NotImplementedError

    @abstractmethod
    async def save_chat_message(self, message: ChatMessage) -> ChatMessageId:
        raise NotImplementedError

    @abstractmethod
    async def delete_chat_message(self, message_id: ChatMessageId) -> None:
        raise NotImplementedError
