from dataclasses import dataclass
from typing import NewType

TagId = NewType("TagId", int)


@dataclass
class Tag:
    """Сущность тега пользователя.

    Тег определяет интересы пользователя('ищу команду', 'ищу романтику', 'ищу друзей').
    """

    id: TagId | None
    name: str
