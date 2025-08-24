import pytest

from app.domain.entities.user import NameDisplay
from tests.factories import make_user


@pytest.mark.parametrize("nickname", ["", None])
def test_creation_of_a_user_without_nickname_and_nickname_display(
    nickname: str | None,
) -> None:
    with pytest.raises(
        ValueError, match="Пользователь не может отображать nickname, если его нет."
    ):
        make_user(nickname=nickname, name_display=NameDisplay.NICKNAME)
