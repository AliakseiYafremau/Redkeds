from typing import Protocol

from redkeds.domain.entities.user import UserId


class IdProvider(Protocol):
    """Manage ID of users."""

    def __call__(self) -> UserId:
        """Return the ID of the current user."""
        ...
