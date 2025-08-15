from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest
from faker import Faker

from app.adapters.exceptions import InvalidPasswordError
from app.adapters.password import PasswordHasher
from app.application.dto.user import LoginUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


async def test_auth_with_same_passwords(
    password_hasher: PasswordHasher, faker: Faker
) -> None:
    # Arrange
    password = faker.password()
    user_id = UserId(uuid4)
    stub_user = Mock(spec=User)
    stub_user.password = password_hasher.hash_password(password)
    stub_user.id = user_id

    mock_user_gateway = AsyncMock()
    mock_user_gateway.get_user_by_email.return_value = stub_user

    auth_interactor = AuthUserInteractor(mock_user_gateway, password_hasher)
    data = LoginUserDTO(
        email=faker.email(),
        password=password,
    )

    # Act
    result = await auth_interactor(data)

    # Assert
    assert user_id == result
    mock_user_gateway.get_user_by_email.assert_called_once_with(data.email)


async def test_auth_with_different_passwords(
    password_hasher: PasswordHasher, faker: Faker
) -> None:
    # Arrange
    user_password = faker.unique.password()
    login_password = faker.unique.password()
    stub_user = Mock(spec=User)
    stub_user.password = password_hasher.hash_password(user_password)

    stub_user_gateway = AsyncMock()
    stub_user_gateway.get_user_by_email.return_value = stub_user

    auth_interactor = AuthUserInteractor(stub_user_gateway, password_hasher)
    data = LoginUserDTO(
        email=faker.email(),
        password=login_password,
    )

    # Act
    with pytest.raises(InvalidPasswordError):
        await auth_interactor(data)
