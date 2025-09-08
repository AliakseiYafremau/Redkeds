from typing import Protocol
from uuid import UUID


class UUIDGenerator(Protocol):
    @staticmethod
    def __call__() -> UUID:
        """Generate a new UUID."""
        ...
