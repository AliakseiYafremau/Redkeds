from app.application.interfaces.common.id_provider import IdProvider
from app.domain.entities.user_id import UserId


class FakeIdProvider(IdProvider):
    """Фейковый провайдер для получения ID."""

    def __init__(self, user_id: UserId) -> None:
        self.user_id = user_id

    def __call__(self) -> UserId:
        """Просто возвращает тот же ID."""
        return self.user_id
