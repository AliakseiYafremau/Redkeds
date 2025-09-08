from typing import Protocol

from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.showcase import Showcase, ShowcaseId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId
from redkeds.domain.entities.user_id import UserId


class ShowcaseGateway(Protocol):
    async def get_showcase_by_user_id(self, user_id: UserId) -> Showcase: ...

    async def get_showcases(
        self,
        exclude_showcase: ShowcaseId | None = None,
        specialization_ids: list[SpecializationId] | None = None,
        city_ids: list[CityId] | None = None,
        tag_ids: list[TagId] | None = None,
        communication_method_ids: list[CommunicationMethodId] | None = None,
    ) -> list[Showcase]: ...

    async def save_showcase(self, showcase: Showcase) -> ShowcaseId: ...

    async def delete_showcase(self, showcase_id: ShowcaseId) -> None: ...
