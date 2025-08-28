from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from redkeds.application.dto.communication_method import CommunicationMethodDTO
from redkeds.application.interactors.communication_method.read import (
    ReadCommunicationMethodsInteractor,
)

communication_method_router = APIRouter(
    prefix="/communication_method",
    tags=["Способы общения"],
)


@communication_method_router.get(
    path="/",
    summary="Получение всех способов общения.",
    description="Возвращает список всех способов общения.",
)
@inject
async def get_communication_method(
    interactor: FromDishka[ReadCommunicationMethodsInteractor],
) -> list[CommunicationMethodDTO]:
    """Получение методов общения."""
    return await interactor()
