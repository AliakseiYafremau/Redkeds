from typing import Protocol


class TransactionManager(Protocol):
    """Интерфейс для управления транзакциями."""

    def commit(self) -> None:
        """Коммитит текущую транзакцию."""
        ...

    def flush(self) -> None:
        """Флашит текущую транзакцию."""
        ...

    def rollback(self) -> None:
        """Откатывает текущую транзакцию."""
        ...
