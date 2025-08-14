from dataclasses import dataclass
from datetime import datetime

from app.domain.entities.chat import ChatId, ChatMessageId
from app.domain.entities.user_id import UserId


@dataclass
class NewChatMessageDTO:
    """DTO для создания нового сообщения."""

    chat_id: ChatId
    text: str


@dataclass
class ReadChatMessageDTO:
    """DTO для чтения сообщения."""

    id: ChatMessageId
    chat_id: ChatId
    sender_id: UserId
    text: str
    timestamp: datetime


@dataclass
class ReadChatDTO:
    """DTO для чтения чата."""

    id: ChatId
    user1_id: UserId
    user2_id: UserId
    messages: list[ReadChatMessageDTO]


@dataclass
class ReadShortChatDTO:
    """DTO для минимального чтения чата."""

    id: ChatId
    user1_id: UserId
    user2_id: UserId
