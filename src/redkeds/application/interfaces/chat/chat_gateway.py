from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.chat import Chat, ChatId
from redkeds.domain.entities.user_id import UserId


class ChatGateway(Protocol):
    @abstractmethod
    async def get_chat_by_id(self, chat_id: ChatId) -> Chat:
        raise NotImplementedError

    @abstractmethod
    async def get_user_chats(self, user_id: UserId) -> list[Chat]:
        raise NotImplementedError

    @abstractmethod
    async def save_chat(self, chat: Chat) -> ChatId:
        raise NotImplementedError

    @abstractmethod
    async def delete_chat(self, chat_id: ChatId) -> None:
        raise NotImplementedError
