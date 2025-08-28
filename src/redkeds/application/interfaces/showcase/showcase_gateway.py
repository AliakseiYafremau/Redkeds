from typing import Protocol

from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.showcase import Showcase, ShowcaseId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId
from redkeds.domain.entities.user_id import UserId


class ShowcaseReader(Protocol):
    """Интерфейс для чтения данных витрины."""

    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase:
        """Получает информацию о витрине по ID пользователя."""
        ...

    async def get_showcases(
        self,
        exclude_showcase: ShowcaseId | None = None,
        specialization_ids: list[SpecializationId] | None = None,
        city_ids: list[CityId] | None = None,
        tag_ids: list[TagId] | None = None,
        communication_method_ids: list[CommunicationMethodId] | None = None,
    ) -> list[Showcase]:
        """Получает все витрины, игнорируя exclude_showcase."""
        ...


class ShowcaseSaver(Protocol):
    """Интерфейс для сохранения витрины."""

    async def save_showcase(self, showcase: Showcase) -> ShowcaseId:
        """Сохраняет обьект витрины."""
        ...


class ShowcaseDeleter(Protocol):
    """Интерфейс для удаления витрины."""

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None:
        """Удаляет обьект витрины."""
        ...
