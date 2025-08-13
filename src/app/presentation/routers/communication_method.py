from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.communication_method import CommunicationMethodDTO
from app.application.interactors.communication_method.read import (
    ReadCommunicationMethodsInteractor,
)

communication_method_router = APIRouter(
    prefix="/communication_method",
    tags=["методы общения"],
)


@communication_method_router.get("/")
@inject
async def get_communication_method(
    interactor: FromDishka[ReadCommunicationMethodsInteractor],
) -> list[CommunicationMethodDTO]:
    """Получение методов общения."""
    return await interactor()
