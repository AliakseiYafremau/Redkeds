from app.adapters.models import UserModel, WorkModel
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.showcase import ShowcaseId, Work, WorkId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


def map_model_to_user(model: UserModel) -> User:
    """Маппит модель пользователя в сущность."""
    if model.name_display is None:
        raise ValueError("Name display cannot be None")
    return User(
        id=UserId(model.id),
        email=model.email,
        username=model.username,
        nickname=model.nickname,
        name_display=model.name_display,
        password=model.password,
        photo=model.photo,
        specialization=[
            SpecializationId(specialization.id)
            for specialization in model.specializations
        ],
        default_photo=model.default_photo,
        city=CityId(model.city_id),
        description=model.description,
        tags=[TagId(tag.id) for tag in model.tags],
        communication_method=CommunicationMethodId(model.communication_method_id),
        status=model.status,
        showcase=ShowcaseId(model.showcase_id)
        if model.showcase_id is not None
        else None,
    )


def map_user_to_model(user: User) -> UserModel:
    """Маппит сущность пользователя в модель."""
    return UserModel(
        id=user.id,
        email=user.email,
        username=user.username,
        nickname=user.nickname,
        name_display=user.name_display,
        password=user.password,
        photo=user.photo,
        default_photo=user.default_photo,
        description=user.description,
        status=user.status,
        city_id=user.city,
        communication_method_id=user.communication_method,
        showcase_id=user.showcase,
    )


def map_model_to_work(model: WorkModel) -> Work:
    """Маппит модель работы витрины в сущность."""
    return Work(
        id=WorkId(model.id),
        showcase_id=ShowcaseId(model.showcase_id),
        title=model.title,
        description=model.description,
        file_path=model.file_path,
    )


def map_work_to_model(work: Work) -> WorkModel:
    """Маппит сущность работы витрины в модель."""
    return WorkModel(
        id=work.id,
        showcase_id=work.showcase_id,
        title=work.title,
        description=work.description,
        file_path=work.file_path,
    )
