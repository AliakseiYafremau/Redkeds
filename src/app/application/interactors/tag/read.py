from app.application.dto.tag import TagDTO
from app.application.interfaces.tag.tag_gateway import TagReader


class ReadTagsInteractor:
    """Интерактор для получения тегов."""

    def __init__(
        self,
        tag_gateway: TagReader,
    ) -> None:
        self._tag_gateway = tag_gateway

    def __call__(self) -> list[TagDTO]:
        """Возвращает данные о тегах."""
        tags = self._tag_gateway.get_tags()
        return [
            TagDTO(
                id=entity.id,
                name=entity.name,
            )
            for entity in tags
        ]
