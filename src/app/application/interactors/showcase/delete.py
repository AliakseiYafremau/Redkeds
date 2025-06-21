from app.application.interfaces.common.transaction import TransactionManager
from app.application.interfaces.showcase.showcase_gateway import ShowcaseDeleter
from app.domain.entities.showcase import ShowcaseId


class DeleteShowcaseInteractor:
    """Интерактор для удаления витрины."""

    def __init__(
        self,
        showcase_gateway: ShowcaseDeleter,
        transaction_manager: TransactionManager,
    ) -> None:
        self._showcase_gateway = showcase_gateway
        self._transactoin_manager = transaction_manager

    async def __call__(self, showcase_id: ShowcaseId) -> None:
        """Удаляет витрину."""
        await self._showcase_gateway.delete_showcase(showcase_id)
        await self._transactoin_manager.commit()
