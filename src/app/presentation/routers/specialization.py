from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.specialization import SpecializationDTO
from app.application.interactors.specialization.read import (
    ReadSpecializationsInteractor,
)

specialization_router = APIRouter(
    prefix="/specializations",
    tags=["Специализации"],
)


@specialization_router.get(
    path="/",
    summary="Получение всех специализаций.",
    description="Возвращает список всех специализаций.",
)
@inject
async def get_specializations(
    interactor: FromDishka[ReadSpecializationsInteractor],
) -> list[SpecializationDTO]:
    """Получение список специализаций."""
    return await interactor()
