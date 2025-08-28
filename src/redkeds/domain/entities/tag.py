from dataclasses import dataclass
from typing import NewType
from uuid import UUID

TagId = NewType("TagId", UUID)


@dataclass
class Tag:
    """Сущность тега пользователя.

    Тег определяет интересы пользователя('ищу команду', 'ищу романтику', 'ищу друзей').
    """

    id: TagId
    name: str
