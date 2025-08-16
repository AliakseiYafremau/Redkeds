import pytest

from app.adapters.password import BcryptPasswordHasher, PasswordHasher


@pytest.fixture(scope="session")
def password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()
