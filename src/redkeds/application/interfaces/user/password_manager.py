from abc import abstractmethod
from typing import Protocol


class PasswordHasher(Protocol):
    @abstractmethod
    def hash_password(self, password: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def verify_password(self, password: str, hashed_password: str) -> bool:
        raise NotImplementedError
