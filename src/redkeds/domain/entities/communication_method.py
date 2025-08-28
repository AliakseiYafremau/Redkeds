from dataclasses import dataclass
from typing import NewType
from uuid import UUID

CommunicationMethodId = NewType("CommunicationMethodId", UUID)


@dataclass
class CommunicationMethod:
    """Сущность предпочтения способа общения пользователя.

    Способ общения определяет предпочтительный способ связи пользователя
    ('онлайн', 'готов к встречам').
    """

    id: CommunicationMethodId | None
    name: str
