from app.domain.entities.chat import Chat, ChatMessage
from app.domain.entities.user_id import UserId
from app.domain.exceptions import AccessDeniedError


def ensure_can_manage_chat(chat: Chat, user_id: UserId) -> bool:
    """Проверяет возможность управление чатом."""
    if str(user_id) not in (str(chat.user1_id), str(chat.user2_id)):
        raise AccessDeniedError("Нет доступа к чату.")
    return True


def ensure_can_manage_chat_message(message: ChatMessage, user_id: UserId) -> bool:
    """Проверяет возможность управления сообщением."""
    if str(message.sender_id) != str(user_id):
        raise AccessDeniedError("Нет доступа к сообщениям.")
    return True
