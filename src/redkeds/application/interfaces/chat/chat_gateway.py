from typing import Protocol

from redkeds.domain.entities.chat import Chat, ChatId
from redkeds.domain.entities.user_id import UserId


class ChatReader(Protocol):
    """Интерфейс для чтения чата."""

    async def get_chat_by_id(self, chat_id: ChatId) -> Chat:
        """Получает чат по ID."""
        ...

    async def get_user_chats(self, user_id: UserId) -> list[Chat]:
        """Получает чат по ID пользователя."""
        ...


class ChatSaver(Protocol):
    """Интерфейс для сохранения чата."""

    async def save_chat(self, chat: Chat) -> ChatId:
        """Сохраняет чат."""
        ...


class ChatDeleter(Protocol):
    """Интерфейс для удаления чата."""

    async def delete_chat(self, chat_id: ChatId) -> None:
        """Удаляет чат."""
        ...
