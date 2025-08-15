import pytest

from app.adapters.password import BcryptPasswordHasher, PasswordHasher


@pytest.fixture
def password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()
