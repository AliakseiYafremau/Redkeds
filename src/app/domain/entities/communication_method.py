from dataclasses import dataclass
from typing import NewType

CommunicationMethodId = NewType("CommunicationMethodId", int)


@dataclass
class CommunicationMethod:
    """Сущность предпочтения способа общения пользователя.

    Способ общения определяет предпочтительный способ связи пользователя
    ('онлайн', 'готов к встречам').
    """

    id: CommunicationMethodId | None
    name: str
