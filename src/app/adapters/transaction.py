from app.application.interfaces.common.transaction import TransactionManager


class FakeSQLTransactionManager(TransactionManager):
    """Моковый SQL менеджер транзакций."""

    async def commit(self) -> None:
        """Коммитит текущую транзакцию."""

    async def flush(self) -> None:
        """Флашит текущую транзакцию."""

    async def rollback(self) -> None:
        """Откатывает текущую транзакцию."""
