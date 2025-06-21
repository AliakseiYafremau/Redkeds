from app.application.interfaces.tag.tag_gateway import TagReader
from app.domain.entities.tag import Tag


class TagGateway(
    TagReader,
):
    """Gateway для работы с тегами."""

    async def get_tags(self) -> list[Tag]:
        """Получает информацию о всех тегах."""
        return []
