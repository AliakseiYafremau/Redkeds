from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from redkeds.adapters.models import ChatMessageModel, ChatModel
from redkeds.application.interfaces.chat.chat_gateway import ChatGateway
from redkeds.application.interfaces.chat.chat_message_gateway import ChatMessageGateway
from redkeds.domain.entities.chat import Chat, ChatId, ChatMessage, ChatMessageId
from redkeds.domain.entities.user_id import UserId


class SQLChatGateway(ChatGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_chat_by_id(self, chat_id: ChatId) -> Chat:
        statement = select(ChatModel).where(ChatModel.id == chat_id)
        result = await self._session.execute(statement)
        chat_model = result.scalar_one_or_none()
        if chat_model is None:
            raise ValueError(f"Chat with id {chat_id} not found")
        return Chat(
            id=ChatId(chat_model.id),
            user1_id=UserId(chat_model.user1_id),
            user2_id=UserId(chat_model.user2_id),
        )

    async def get_user_chats(self, user_id: UserId) -> list[Chat]:
        statement = select(ChatModel).where(
            (ChatModel.user1_id == user_id) | (ChatModel.user2_id == user_id)
        )
        result = await self._session.execute(statement)
        chat_models = result.scalars().all()
        return [
            Chat(
                id=ChatId(model.id),
                user1_id=UserId(model.user1_id),
                user2_id=UserId(model.user2_id),
            )
            for model in chat_models
        ]

    async def save_chat(self, chat: Chat) -> ChatId:
        chat_model = ChatModel(
            id=chat.id,
            user1_id=chat.user1_id,
            user2_id=chat.user2_id,
        )
        self._session.add(chat_model)
        return chat.id

    async def delete_chat(self, chat_id: ChatId) -> None:
        """Удаляет чат по id."""
        statement = select(ChatModel).where(ChatModel.id == chat_id)
        result = await self._session.execute(statement)
        chat_model = result.scalar_one_or_none()
        if chat_model is None:
            raise ValueError(f"Chat with id {chat_id} not found")
        await self._session.delete(chat_model)


class SQLChatMessageGateway(ChatMessageGateway):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_chat_message_by_id(self, message_id: ChatMessageId) -> ChatMessage:
        statement = select(ChatMessageModel).where(ChatMessageModel.id == message_id)
        result = await self._session.execute(statement)
        message_model = result.scalar_one_or_none()
        if message_model is None:
            raise ValueError(f"ChatMessage with id {message_id} not found")
        return ChatMessage(
            id=ChatMessageId(message_model.id),
            chat_id=ChatId(message_model.chat_id),
            sender_id=UserId(message_model.sender_id),
            text=message_model.text,
            timestamp=message_model.timestamp,
        )

    async def get_chat_messages_by_chat(self, chat_id: ChatId) -> list[ChatMessage]:
        statement = select(ChatMessageModel).where(ChatMessageModel.chat_id == chat_id)
        result = await self._session.execute(statement)
        message_models = result.scalars().all()
        return [
            ChatMessage(
                id=ChatMessageId(model.id),
                chat_id=ChatId(model.chat_id),
                sender_id=UserId(model.sender_id),
                text=model.text,
                timestamp=model.timestamp,
            )
            for model in message_models
        ]

    async def save_chat_message(self, message: ChatMessage) -> ChatMessageId:
        message_model = ChatMessageModel(
            id=message.id,
            chat_id=message.chat_id,
            sender_id=message.sender_id,
            text=message.text,
            timestamp=message.timestamp,
        )
        self._session.add(message_model)
        return message.id

    async def delete_chat_message(self, message_id: ChatMessageId) -> None:
        statement = select(ChatMessageModel).where(ChatMessageModel.id == message_id)
        result = await self._session.execute(statement)
        message_model = result.scalar_one_or_none()
        if message_model is None:
            raise ValueError(f"ChatMessage with id {message_id} not found")
        await self._session.delete(message_model)
