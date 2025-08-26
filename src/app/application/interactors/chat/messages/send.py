from datetime import UTC, datetime

from app.application.dto.chat import NewChatMessageDTO
from app.application.interfaces.chat.chat_gateway import ChatReader
from app.application.interfaces.chat.chat_message_gateway import ChatMessageSaver
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.chat import ChatMessage, ChatMessageId
from app.domain.services.chat_service import ensure_can_manage_chat
from app.logs import get_logger

logger = get_logger(__name__)


class SendChatMessageInteractor:
    """Интерактор для отправки сообщений."""

    def __init__(
        self,
        id_provider: IdProvider,
        user_gateway: UserReader,
        chat_gateway: ChatReader,
        message_gateway: ChatMessageSaver,
        uuid_generator: UUIDGenerator,
        transaction_manager: TransactionManager,
    ) -> None:
        self._id_provider = id_provider
        self._user_gateway = user_gateway
        self._chat_gateway = chat_gateway
        self._message_gateway = message_gateway
        self._uuid_generator = uuid_generator
        self._transaction_manager = transaction_manager

    async def __call__(
        self,
        data: NewChatMessageDTO,
    ) -> ChatMessageId:
        """Добавляет сообщение в чат."""
        user_id = self._id_provider()
        chat = await self._chat_gateway.get_chat_by_id(data.chat_id)
        logger.info(chat.user1_id)
        logger.info(user_id)
        ensure_can_manage_chat(chat, user_id)
        message_id = ChatMessageId(self._uuid_generator())
        message = ChatMessage(
            id=message_id,
            sender_id=user_id,
            chat_id=data.chat_id,
            text=data.text,
            timestamp=datetime.now(tz=UTC),
        )
        await self._message_gateway.save_chat_message(message)
        await self._transaction_manager.commit()
        return message_id
