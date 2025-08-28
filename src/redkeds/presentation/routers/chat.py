from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from redkeds.application.dto.chat import ReadShortChatDTO
from redkeds.application.interactors.chat.create import CreateChatInteractor
from redkeds.application.interactors.chat.delete import DeleteChatInteractor
from redkeds.application.interactors.chat.read import ReadUserChatInteractor
from redkeds.domain.entities.chat import ChatId
from redkeds.domain.entities.user_id import UserId

chat_router = APIRouter(
    prefix="/chat",
    tags=["Чат"],
)


@chat_router.post(
    path="/",
    summary="Создание чата.",
    description=(
        "Создания чата с определенным пользователем. "
        "После запроса создается чат пользователя, "
        "который послал запрос с пользователем, посланного **user_id**."
    ),
)
@inject
async def create_chat(
    user_id: UserId,
    interactor: FromDishka[CreateChatInteractor],
) -> ChatId:
    """Создание чата."""
    return await interactor(user_id)


@chat_router.get(
    path="/",
    summary="Получение всех чатов пользователя.",
    description="Возвращается список всех доступных пользователю чатов.",
)
@inject
async def get_chats(
    interactor: FromDishka[ReadUserChatInteractor],
) -> list[ReadShortChatDTO]:
    """Получение всех чатов пользователя."""
    return await interactor()


@chat_router.delete(
    path="/",
    summary="Удаление чата.",
    description="Удаления чата пользователя. Чат удаляется у всех участников чата.",
)
@inject
async def delete_chat(
    chat_id: ChatId,
    interactor: FromDishka[DeleteChatInteractor],
) -> None:
    """Удаление чата."""
    await interactor(chat_id)
