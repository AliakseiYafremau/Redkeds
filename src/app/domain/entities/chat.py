from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from .user_id import UserId

ChatId = NewType("ChatId", UUID)
ChatMessageId = NewType("ChatMessageId", UUID)


@dataclass
class Chat:
    """Сущность чата между двумя пользователями."""

    id: ChatId | None
    user1_id: UserId
    user2_id: UserId


@dataclass
class ChatMessage:
    """Сущность сообщения в чате."""

    id: ChatMessageId | None
    chat_id: ChatId
    sender_id: UserId
    text: str
    timestamp: datetime
