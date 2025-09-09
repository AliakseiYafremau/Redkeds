from abc import abstractmethod
from typing import Protocol
from uuid import UUID


class UUIDGenerator(Protocol):
    @abstractmethod
    @staticmethod
    def __call__() -> UUID:
        """Generate a new UUID."""
        raise NotImplementedError
