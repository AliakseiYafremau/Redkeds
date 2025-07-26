from app.application.interfaces.chat.chat_gateway import ChatSaver
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.domain.entities.chat import Chat, ChatId
from app.domain.entities.user_id import UserId


class CreateChatInteractor:
    """Интерактор для создания чата."""

    def __init__(
        self,
        id_provider: IdProvider,
        chat_gateway: ChatSaver,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._id_provider = id_provider
        self._chat_gateway = chat_gateway
        self._uuid_generator = uuid_generator

    async def __call__(self, second_user_id: UserId) -> ChatId:
        """Создает чат для двух пользователей."""
        first_user_id = self._id_provider()
        chat = Chat(
            id=ChatId(self._uuid_generator()),
            user1_id=first_user_id,
            user2_id=second_user_id,
        )
        return await self._chat_gateway.save_chat(chat)
