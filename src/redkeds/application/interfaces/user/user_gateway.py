from abc import abstractmethod
from typing import Protocol

from redkeds.domain.entities.user import User
from redkeds.domain.entities.user_id import UserId


class UserGateway(Protocol):
    @abstractmethod
    async def save_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User:
        raise NotImplementedError

    @abstractmethod
    async def update_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete_user(self, user_id: UserId) -> None:
        raise NotImplementedError
