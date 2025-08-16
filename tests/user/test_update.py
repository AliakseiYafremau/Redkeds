from collections.abc import Callable
from unittest.mock import create_autospec
from uuid import uuid4

import pytest
from faker import Faker

from app.application.dto.user import UpdateUserDTO
from app.application.interactors.user.update import UpdateUserInteractor, UserGateway
from app.application.interfaces.common.file_gateway import FileManager
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.domain.entities.file_id import FileId
from app.domain.entities.user import User
from tests.factories import make_user


@pytest.fixture(scope="module")
def make_update_interactor() -> None:
    def factory(user: User):
        mock_user_gateway = create_autospec(UserGateway)
        mock_id_provider = create_autospec(IdProvider)
        mock_file_manager = create_autospec(FileManager)
        mock_transaction_manager = create_autospec(TransactionManager)

        mock_user_gateway.get_user_by_id.return_value = user

        return UpdateUserInteractor(
            mock_user_gateway,
            mock_id_provider,
            mock_file_manager,
            mock_transaction_manager,
        )

    return factory


async def test_update_user(
    make_update_interactor: Callable[[User], UpdateUserInteractor], faker: Faker
) -> None:
    # Arrange
    new_email = faker.email()
    new_username = faker.name()
    new_nickname = faker.user_name()
    new_description = faker.text(max_nb_chars=20)
    new_status = faker.text(max_nb_chars=10)

    user = make_user()

    update_interactor = make_update_interactor(user)
    data = UpdateUserDTO(
        email=new_email,
        username=new_username,
        nickname=new_nickname,
        description=new_description,
        status=new_status,
    )

    # Act
    await update_interactor(data)

    # Assert
    update_interactor._file_manager.update.assert_not_called()
    update_interactor._transaction_manager.commit.assert_called_once()

    new_user: User = update_interactor._user_gateway.update_user.call_args.args[0]
    assert new_user.email == new_email
    assert new_user.username == new_username
    assert new_user.nickname == new_nickname
    assert new_user.description == new_description
    assert new_user.status == new_status


async def test_update_photo_of_user_with_photo(
    make_update_interactor: Callable[[User], UpdateUserInteractor], faker: Faker
) -> None:
    # Arrange
    initial_photo_id = FileId(uuid4())
    new_photo = faker.binary()

    user = make_user(photo=initial_photo_id)

    update_interactor = make_update_interactor(user)
    data = UpdateUserDTO(
        photo=new_photo,
    )

    # Act
    await update_interactor(data)

    # Assert
    update_interactor._file_manager.update.assert_called_once_with(
        initial_photo_id, new_photo
    )
    update_interactor._transaction_manager.commit.assert_called_once()

    new_user: User = update_interactor._user_gateway.update_user.call_args.args[0]
    assert new_user.photo == initial_photo_id


async def test_update_photo_of_user_without_photo(
    make_update_interactor: Callable[[User], UpdateUserInteractor],
    faker: Faker,
) -> None:
    # Arrange
    new_photo_id = FileId(uuid4())
    new_photo = faker.binary()

    user = make_user(photo=None)

    update_interactor = make_update_interactor(user)
    update_interactor._file_manager.save.return_value = new_photo_id
    data = UpdateUserDTO(
        photo=new_photo,
    )

    # Act
    await update_interactor(data)

    # Assert
    update_interactor._file_manager.save.assert_called_once_with(new_photo)
    update_interactor._transaction_manager.commit.assert_called_once()

    new_user: User = update_interactor._user_gateway.update_user.call_args.args[0]
    assert new_user.photo == new_photo_id
