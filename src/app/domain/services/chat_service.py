from app.domain.entities.chat import Chat, ChatMessage
from app.domain.entities.user_id import UserId
from app.domain.exceptions import CannotManageChatError, CannotManageChatMessageError


def ensure_can_manage_chat(chat: Chat, user_id: UserId) -> bool:
    """Проверяет возможность управление чатом."""
    if (chat.user1_id != user_id) or (chat.user2_id != user_id):
        raise CannotManageChatError
    return True


def ensure_can_manage_chat_message(message: ChatMessage, user_id: UserId) -> bool:
    """Проверяет возможность управления сообщением."""
    if message.sender_id != user_id:
        raise CannotManageChatMessageError
    return True
