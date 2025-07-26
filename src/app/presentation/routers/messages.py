from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.chat import NewChatMessageDTO, ReadChatDTO
from app.application.interactors.chat.messages.delete import DeleteChatMessageInteractor
from app.application.interactors.chat.messages.read import ReadMessageInteractor
from app.application.interactors.chat.messages.send import SendChatMessageInteractor
from app.domain.entities.chat import ChatId, ChatMessageId

message_router = APIRouter(prefix="/message", tags=["Чат"])


@message_router.post("/")
@inject
async def send_message(
    message_data: NewChatMessageDTO,
    interactor: FromDishka[SendChatMessageInteractor],
) -> ChatMessageId:
    """Отправка сообщения."""
    return await interactor(message_data)


@message_router.get("/")
@inject
async def get_messages(
    chat_id: ChatId,
    interactor: FromDishka[ReadMessageInteractor],
) -> ReadChatDTO:
    """Чтение сообщения."""
    return await interactor(chat_id)


@message_router.delete("/")
@inject
async def delete_message(
    message_id: ChatMessageId,
    interactor: FromDishka[DeleteChatMessageInteractor],
) -> None:
    """Удаление сообщение."""
    await interactor(message_id)
