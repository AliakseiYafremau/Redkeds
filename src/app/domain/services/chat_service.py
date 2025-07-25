from app.domain.entities.chat import Chat, UserId
from app.domain.exceptions import CannotManageChatError


def ensure_can_manage_chat(chat: Chat, user_id: UserId) -> bool:
    """Проверяет возможность управление чатом."""
    if (chat.user1_id != user_id) or (chat.user2_id != user_id):
        raise CannotManageChatError
    return True
