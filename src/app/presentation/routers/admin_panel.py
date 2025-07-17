from typing import ClassVar
from uuid import uuid4

from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine

from app.adapters.models import (
    CityModel,
    CommunicationMethodModel,
    SpecializationModel,
    TagModel,
)


class IdGenerateView(ModelView):
    """Базовая модель, генерирующая ID."""

    async def on_model_change(self, data, model, is_created, request) -> None:  # noqa: ANN001, ARG002
        """Генерирует новый UUID."""
        if is_created:
            data["id"] = uuid4()


class TagAdmin(IdGenerateView, model=TagModel):
    """Модель тега в админ-панели."""

    name = "Тег"
    name_plural = "Теги"
    column_list: ClassVar[list] = [TagModel.name]


class CityAdmin(IdGenerateView, model=CityModel):
    """Модель города в админ-панели."""

    name = "Город"
    name_plural = "Города"
    column_list: ClassVar[list] = [CityModel.name]


class SpecializationAdmin(IdGenerateView, model=SpecializationModel):
    """Модель специализации в админ-панели."""

    name = "Специализация"
    name_plural = "Специализации"
    column_list: ClassVar[list] = [SpecializationModel.name]


class CommunicationMethodAdmin(IdGenerateView, model=CommunicationMethodModel):
    """Модель предпочтения общения в админ-панели."""

    name = "Метод общения"
    name_plural = "Методы общения"
    column_list: ClassVar[list] = [CommunicationMethodModel.name]


def connect_admin_panel(app: FastAPI, engine: AsyncEngine) -> None:
    """Подключение админ-панели."""
    admin = Admin(
        app=app,
        base_url="/admin",
        engine=engine,
    )

    admin.add_view(CityAdmin)
    admin.add_view(TagAdmin)
    admin.add_view(SpecializationAdmin)
    admin.add_view(CommunicationMethodAdmin)
