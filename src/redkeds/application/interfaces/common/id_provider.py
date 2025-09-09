from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.user import UserId


class IdProvider(Protocol):
    """Manage ID of users."""

    @abstractmethod
    def __call__(self) -> UserId:
        """Return the ID of the current user."""
        raise NotImplementedError
