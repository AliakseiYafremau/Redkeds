from redkeds.domain.exceptions import WeakPasswordError


def validate_password(password: str) -> bool:
    """Проверяет пароль на валидность.

    Требования: не менее 5 символов, минимум одна цифра и одна буква.
    """
    if len(password) < 5:
        raise WeakPasswordError("Пароль должен содержать не менее 5 символов.")

    has_digit = any(c.isdigit() for c in password)
    has_alpha = any(c.isalpha() for c in password)

    if not (has_digit and has_alpha):
        raise WeakPasswordError(
            "Пароль должен содержать как минимум одну букву и одну цифру."
        )
    return True
