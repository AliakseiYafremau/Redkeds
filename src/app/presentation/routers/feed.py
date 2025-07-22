from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, HTTPException

from app.adapters.exceptions import (
    ShowcaseDoesNotExistError,
    WorkDoesNotExistError,
)
from app.application.dto.work import NewWorkDTO, ReadWorkDTO, UpdateWorkDTO
from app.application.interactors.work.create import CreateWorkInteractor
from app.application.interactors.work.delete import DeleteWorkInteractor
from app.application.interactors.work.read import (
    ReadAllWorksInteractor,
    ReadWorkInteractor,
)
from app.application.dto.showcase import ReadShowcaseDTO
from app.application.interactors.recommendation_feed.read import ReadRecommendationFeed
from app.application.interactors.work.update import UpdateWorkInteractor
from app.domain.entities.showcase import ShowcaseId, WorkId
from app.adapters.exceptions import UserDoesNotExistError
from app.domain.exceptions import CannotManageWorkError

feed_router = APIRouter(prefix="/feed", tags=["Работа с лентой рекомендаций"])


@feed_router.get("/")
@inject
async def read_feed(
    interactor: FromDishka[ReadRecommendationFeed],
) -> list[ReadShowcaseDTO]:
    """Возвращает ленту из витрин пользователей."""
    try:
        return await interactor()
    except UserDoesNotExistError:
        HTTPException(
            status_code=404,
            detail="Пользователь не найден."
        )
