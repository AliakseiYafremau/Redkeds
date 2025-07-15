from app.adapters.models import UserModel
from app.domain.entities.city import CityId
from app.domain.entities.communication_method import CommunicationMethodId
from app.domain.entities.showcase import ShowcaseId
from app.domain.entities.specialization import SpecializationId
from app.domain.entities.tag import TagId
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


def map_model_to_user(model: UserModel) -> User:
    """Маппит модель пользователя в сущность."""
    return User(
        id=UserId(model.id),
        username=model.username,
        password=model.password,
        photo=model.photo,
        specialization=[
            SpecializationId(specialization.id)
            for specialization in model.specializations
        ],
        city=CityId(model.city_id),
        description=model.description,
        tags=[TagId(tag.id) for tag in model.tags],
        communication_method=CommunicationMethodId(model.communication_method_id),
        status=model.status,
        showcase=ShowcaseId(model.showcase_id),
    )


def map_user_to_model(user: User) -> UserModel:
    """Маппит сущность пользователя в модель."""
    return UserModel(
        id=user.id,
        username=user.username,
        password=user.password,
        photo=user.photo,
        description=user.description,
        status=user.status,
        city_id=user.city,
        communication_method_id=user.communication_method,
        showcase_id=user.showcase,
    )
