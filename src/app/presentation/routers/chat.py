from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.chat import ReadShortChatDTO
from app.application.interactors.chat.create import CreateChatInteractor
from app.application.interactors.chat.delete import DeleteChatInteractor
from app.application.interactors.chat.read import ReadUserChatInteractor
from app.domain.entities.chat import ChatId
from app.domain.entities.user_id import UserId

chat_router = APIRouter(
    prefix="/chat",
    tags=["Чат"],
)


@chat_router.post("/")
@inject
async def create_chat(
    chat_data: UserId,
    interactor: FromDishka[CreateChatInteractor],
) -> ChatId:
    """Создание чата."""
    return await interactor(chat_data)


@chat_router.get("/")
@inject
async def get_chats(
    interactor: FromDishka[ReadUserChatInteractor],
) -> list[ReadShortChatDTO]:
    """Получение всех чатов пользователя."""
    return await interactor()


@chat_router.delete("/")
@inject
async def delete_chat(
    chat_id: ChatId,
    interactor: FromDishka[DeleteChatInteractor],
) -> None:
    """Удаление чата."""
    await interactor(chat_id)
