from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.common.uuid_generator import UUIDGenerator
from app.application.interfaces.showcase.showcase_gateway import ShowcaseSaver
from app.application.interfaces.user.user_gateway import UserReader
from app.domain.entities.showcase import Showcase, ShowcaseId
from app.domain.services.showcase import ensure_can_create_showcase


class CreateShowcaseInteractor:
    """Интерактор для создания витрины для пользователя."""

    def __init__(
        self,
        showcase_gateway: ShowcaseSaver,
        user_gateway: UserReader,
        id_provider: IdProvider,
        uuid_generator: UUIDGenerator,
        transaction_manager: TransactionManager,
    ) -> None:
        self._showcase_gateway = showcase_gateway
        self._user_gateway = user_gateway
        self._id_provider = id_provider
        self._uuid_generator = uuid_generator
        self._transaction_manager = transaction_manager

    def __call__(self) -> ShowcaseId:
        """Создает и сохраняет новую витрину."""
        showcase_id = ShowcaseId(self._uuid_generator())
        user_id = self._id_provider()
        user = self._user_gateway.get_user_by_id(user_id)
        ensure_can_create_showcase(user)
        showcase = Showcase(
            id=showcase_id,
            owner_id=user_id,
        )
        self._showcase_gateway.save_showcase(showcase)
        self._transaction_manager.commit()
        return showcase_id
