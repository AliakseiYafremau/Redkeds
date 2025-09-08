from redkeds.application.dto.tag import TagDTO
from redkeds.application.interfaces.tag.tag_gateway import TagGateway


class ReadTagsInteractor:
    """Интерактор для получения тегов."""

    def __init__(
        self,
        tag_gateway: TagGateway,
    ) -> None:
        self._tag_gateway = tag_gateway

    async def __call__(self) -> list[TagDTO]:
        """Возвращает данные о тегах."""
        tags = await self._tag_gateway.get_tags()
        return [
            TagDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in tags
        ]
