from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.common.transaction import TransactionManager


class SQLTransactionManager(TransactionManager):
    """Менеджер sqlalchemy-транзакций."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        """Коммитит текущую транзакцию."""
        await self._session.commit()

    async def flush(self) -> None:
        """Флашит текущую транзакцию."""
        await self._session.flush()

    async def rollback(self) -> None:
        """Откатывает текущую транзакцию."""
        await self._session.rollback()
