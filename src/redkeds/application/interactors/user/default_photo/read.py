from redkeds.application.interfaces.user.default_photo_gateway import (
    DefaultPhotoGateway,
)
from redkeds.domain.entities.file_id import FileId


class ReadDefaultPhotoInteractor:
    """Интерактор для получения фотографии по умолчанию пользователя."""

    def __init__(self, default_photo_gateway: DefaultPhotoGateway) -> None:
        self._default_photo_gateway = default_photo_gateway

    async def __call__(self) -> list[FileId]:
        """Возвращает дефолтные фото."""
        return await self._default_photo_gateway.get_default_photos()
