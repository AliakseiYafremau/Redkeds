from uuid import uuid4

from faker import Faker

from redkeds.domain.entities.city import CityId
from redkeds.domain.entities.communication_method import CommunicationMethodId
from redkeds.domain.entities.file_id import FileId
from redkeds.domain.entities.showcase import Showcase, ShowcaseId
from redkeds.domain.entities.specialization import SpecializationId
from redkeds.domain.entities.tag import TagId
from redkeds.domain.entities.user import NameDisplay, User
from redkeds.domain.entities.user_id import UserId


def make_user(
    user_id: UserId | None = None,
    email: str | None = None,
    username: str | None = None,
    nickname: str | None = None,
    name_display: NameDisplay = NameDisplay.USERNAME,
    password: str | None = None,
    photo: FileId | None = None,
    default_photo: FileId | None = None,
    specialization: list[SpecializationId] | None = None,
    city: CityId | None = None,
    description: str | None = None,
    tags: list[TagId] | None = None,
    communication_method: CommunicationMethodId | None = None,
    status: str | None = None,
    showcase: ShowcaseId | None = None,
) -> User:
    faker = Faker()
    return User(
        id=user_id or UserId(uuid4()),
        email=email or faker.email(),
        username=username or faker.name(),
        nickname=nickname,
        name_display=name_display,
        password=password or faker.password(),
        photo=photo,
        default_photo=default_photo,
        specialization=specialization or [],
        city=city or CityId(uuid4()),
        description=description or faker.text(max_nb_chars=100),
        tags=tags or [],
        communication_method=communication_method or CommunicationMethodId(uuid4()),
        status=status,
        showcase=showcase,
    )


def make_showcase(
    showcase_id: ShowcaseId | None = None,
) -> Showcase:
    """Фабрика для витрины пользователя."""
    return Showcase(
        id=showcase_id or ShowcaseId(uuid4()),
    )
