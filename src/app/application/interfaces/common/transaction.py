from typing import Protocol


class TransactionManager(Protocol):
    """Интерфейс для управления транзакциями."""

    async def commit(self) -> None:
        """Коммитит текущую транзакцию."""
        ...

    async def flush(self) -> None:
        """Флашит текущую транзакцию."""
        ...

    async def rollback(self) -> None:
        """Откатывает текущую транзакцию."""
        ...
