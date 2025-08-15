from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from app.adapters.exceptions import InvalidPasswordError
from app.adapters.password import PasswordHasher
from app.application.dto.user import LoginUserDTO
from app.application.interactors.user.auth import AuthUserInteractor
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId


async def test_auth_with_same_passwords(password_hasher: PasswordHasher) -> None:
    user_id = UserId(uuid4)
    stub_user = Mock(spec=User)
    stub_user.password = password_hasher.hash_password("1234")
    stub_user.id = user_id

    stub_user_gateway = AsyncMock()
    stub_user_gateway.get_user_by_email.return_value = stub_user

    auth_interactor = AuthUserInteractor(stub_user_gateway, password_hasher)
    data = LoginUserDTO(
        email="123@gmail.com",
        password="1234",
    )

    result = await auth_interactor(data)

    assert user_id == result


async def test_auth_with_different_passwords(password_hasher: PasswordHasher) -> None:
    stub_user = Mock(spec=User)
    stub_user.password = password_hasher.hash_password("1234")

    stub_user_gateway = AsyncMock()
    stub_user_gateway.get_user_by_email.return_value = stub_user

    auth_interactor = AuthUserInteractor(stub_user_gateway, password_hasher)
    data = LoginUserDTO(
        email="123@gmail.com",
        password="different",
    )

    with pytest.raises(InvalidPasswordError):
        await auth_interactor(data)
