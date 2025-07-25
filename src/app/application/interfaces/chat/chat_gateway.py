from typing import Protocol

from app.domain.entities.chat import Chat, ChatId


class ChatReader(Protocol):
    """Интерфейс для чтения чата."""

    async def get_chat_by_id(self, chat_id: ChatId) -> Chat:
        """Получает чат по ID."""
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
