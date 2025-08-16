from collections.abc import Callable
from unittest.mock import create_autospec
from uuid import uuid4

import pytest

from app.application.interactors.user.delete import (
    DeleteUserInteractor,
    ShowcaseGateway,
    UserGateway,
)
from app.application.interfaces.common.file_gateway import FileManager
from app.application.interfaces.common.id_provider import IdProvider
from app.application.interfaces.common.transaction import TransactionManager
from app.domain.entities.file_id import FileId
from app.domain.entities.showcase import Showcase
from app.domain.entities.user import User
from app.domain.entities.user_id import UserId
from tests.factories import make_showcase, make_user


@pytest.fixture(scope="module")
def make_delete_interactor() -> Callable[[Showcase, User], DeleteUserInteractor]:
    def factory(showcase: Showcase, user: User):
        mock_showcase_gateway = create_autospec(ShowcaseGateway, instance=True)
        mock_user_gateway = create_autospec(UserGateway, instance=True)
        mock_file_manager = create_autospec(FileManager, instance=True)
        mock_id_provider = create_autospec(IdProvider, instance=True)
        mock_transaction_manager = create_autospec(TransactionManager, instance=True)

        mock_showcase_gateway.get_showcase_by_user_id.return_value = showcase
        mock_user_gateway.get_user_by_id.return_value = user
        mock_id_provider.return_value = user.id

        return DeleteUserInteractor(
            mock_user_gateway,
            mock_showcase_gateway,
            mock_id_provider,
            mock_file_manager,
            mock_transaction_manager,
        )

    return factory


async def test_delete_user(
    make_delete_interactor: Callable[[Showcase, User], DeleteUserInteractor],
) -> None:
    # Arrange
    showcase = make_showcase()

    user_id = UserId(uuid4())
    photo = FileId(uuid4())
    user = make_user(user_id=user_id, showcase=showcase.id, photo=photo)

    delete_interactor = make_delete_interactor(showcase, user)

    # Act
    await delete_interactor()

    # Assert
    delete_interactor._user_gateway.delete_user.assert_called_once_with(user_id)
    delete_interactor._showcase_gateway.delete_showcase.assert_called_once_with(
        showcase.id
    )
    delete_interactor._file_manager.delete.assert_called_once_with(photo)
    delete_interactor._transaction_manager.commit.assert_called_once()


async def test_delete_user_without_photo(
    make_delete_interactor: Callable[[Showcase, User], DeleteUserInteractor],
) -> None:
    # Arrange
    showcase = make_showcase()

    user_id = UserId(uuid4())
    user = make_user(user_id=user_id, showcase=showcase.id)

    delete_interactor = make_delete_interactor(showcase, user)

    # Act
    await delete_interactor()

    # Assert
    delete_interactor._user_gateway.delete_user.assert_called_once_with(user_id)
    delete_interactor._showcase_gateway.delete_showcase.assert_called_once_with(
        showcase.id
    )
    delete_interactor._file_manager.delete.assert_not_called()
    delete_interactor._transaction_manager.commit.assert_called_once()
