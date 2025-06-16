def validate_password(password: str) -> bool:
    """Проверяет пароль на валидность.

    Требования: не менее 5 символов, минимум одна цифра и одна буква.
    """
    if len(password) < 5:
        return False
    has_digit = any(c.isdigit() for c in password)
    has_alpha = any(c.isalpha() for c in password)
    return has_digit and has_alpha
