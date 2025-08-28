from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from redkeds.application.dto.chat import NewChatMessageDTO, ReadChatDTO
from redkeds.application.interactors.chat.messages.delete import (
    DeleteChatMessageInteractor,
)
from redkeds.application.interactors.chat.messages.read import ReadMessageInteractor
from redkeds.application.interactors.chat.messages.send import SendChatMessageInteractor
from redkeds.domain.entities.chat import ChatId, ChatMessageId

message_router = APIRouter(prefix="/message", tags=["Чат"])


@message_router.post(
    path="/",
    summary="Отправка сообщения.",
    description="Отправляет сообщение в указанный чат.",
)
@inject
async def send_message(
    message_data: NewChatMessageDTO,
    interactor: FromDishka[SendChatMessageInteractor],
) -> ChatMessageId:
    """Отправка сообщения."""
    return await interactor(message_data)


@message_router.get(
    path="/",
    summary="Получение всех сообщений чата.",
    description="Возвращает все сообщения чата.",
)
@inject
async def get_messages(
    chat_id: ChatId,
    interactor: FromDishka[ReadMessageInteractor],
) -> ReadChatDTO:
    """Чтение сообщения."""
    return await interactor(chat_id)


@message_router.delete(
    path="/", summary="Удаление сообщения.", description="Удаляет сообщение из чата."
)
@inject
async def delete_message(
    message_id: ChatMessageId,
    interactor: FromDishka[DeleteChatMessageInteractor],
) -> None:
    """Удаление сообщение."""
    await interactor(message_id)
