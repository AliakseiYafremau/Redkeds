from typing import Protocol

from redkeds.domain.entities.chat import Chat, ChatId
from redkeds.domain.entities.user_id import UserId


class ChatGateway(Protocol):
    async def get_chat_by_id(self, chat_id: ChatId) -> Chat: ...

    async def get_user_chats(self, user_id: UserId) -> list[Chat]: ...

    async def save_chat(self, chat: Chat) -> ChatId: ...

    async def delete_chat(self, chat_id: ChatId) -> None: ...
