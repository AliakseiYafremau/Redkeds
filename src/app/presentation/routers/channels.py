from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.channel import ChannelDTO
from app.application.interactors.channel.read import ReadChannelsInteractor

channels_router = APIRouter(
    prefix="/channels",
    tags=["методы общения"],
)


@channels_router.get("/")
@inject
async def get_channels(
        interactor: FromDishka[ReadChannelsInteractor]
) -> list[ChannelDTO]:
    """Получение методов общения."""
    return await interactor()
