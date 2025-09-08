from collections.abc import Callable
from unittest.mock import create_autospec
from uuid import uuid4

import pytest
from faker import Faker

from redkeds.adapters.exceptions import InvalidPasswordError
from redkeds.adapters.password import PasswordHasher
from redkeds.application.dto.user import LoginUserDTO
from redkeds.application.interactors.user.auth import AuthUserInteractor
from redkeds.application.interfaces.user.user_gateway import UserGateway
from redkeds.domain.entities.user import User
from redkeds.domain.entities.user_id import UserId
from tests.factories import make_user


@pytest.fixture(scope="module")
def make_auth_interactor(
    password_hasher: PasswordHasher,
) -> Callable[[User], AuthUserInteractor]:
    def factory(user: User):
        mock_user_gateway = create_autospec(spec=UserGateway)
        mock_user_gateway.get_user_by_email.return_value = user
        return AuthUserInteractor(
            mock_user_gateway,
            password_hasher,
        )

    return factory


async def test_user_authentication_with_correct_password(
    make_auth_interactor: Callable[[User], AuthUserInteractor],
    password_hasher: PasswordHasher,
    faker: Faker,
) -> None:
    # Arrange
    password = faker.password()
    user_id = UserId(uuid4())
    hashed_password = password_hasher.hash_password(password)
    user = make_user(user_id=user_id, password=hashed_password)

    auth_interactor = make_auth_interactor(user)
    data = LoginUserDTO(
        email=faker.email(),
        password=password,
    )

    # Act
    result = await auth_interactor(data)

    # Assert
    assert user_id == result
    auth_interactor._user_gateway.get_user_by_email.assert_called_once_with(data.email)


async def test_user_authentication_with_incorrect_password(
    make_auth_interactor: Callable[[User], AuthUserInteractor],
    password_hasher: PasswordHasher,
    faker: Faker,
) -> None:
    # Arrange
    user_email = faker.email()
    user_password = faker.unique.password()
    login_password = faker.unique.password()
    hashed_password = password_hasher.hash_password(user_password)
    user = make_user(email=user_email, password=hashed_password)

    auth_interactor = make_auth_interactor(user)
    data = LoginUserDTO(
        email=user_email,
        password=login_password,
    )

    # Act
    with pytest.raises(InvalidPasswordError):
        await auth_interactor(data)

    # Assert
    auth_interactor._user_gateway.get_user_by_email.assert_called_once_with(user_email)
