from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dto.city import CityDTO
from app.application.interactors.city.read import (
    ReadCitiesInteractor,
)

city_router = APIRouter(
    prefix="/cities",
    tags=["Города"],
)


@city_router.get("/")
@inject
async def get_cities(
    interactor: FromDishka[ReadCitiesInteractor],
) -> list[CityDTO]:
    """Получение списка городов."""
    return await interactor()
