from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine

from app.adapters.models import (
    CityModel,
    CommunicationMethodModel,
    SpecializationModel,
    TagModel,
)


class CityAdmin(ModelView, model=CityModel):
    """Модель города в админ-панели."""

    form_include_pk = True


class TagAdmin(ModelView, model=TagModel):
    """Модель тега в админ-панели."""

    form_include_pk = True


class SpecializationAdmin(ModelView, model=SpecializationModel):
    """Модель специализации в админ-панели."""

    form_include_pk = True


class CommunicationMethodAdmin(ModelView, model=CommunicationMethodModel):
    """Модель предпочтения общения в админ-панели."""

    form_include_pk = True


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
