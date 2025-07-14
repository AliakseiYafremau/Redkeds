import logging


def get_logger(name: str) -> logging.Logger:
    """Возвращает базовый логгер."""
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        (
            "[%(levelname)s] [%(asctime)s] "
            "[%(module)s:%(funcName)s:%(lineno)s] - %(message)s"
        ),
    )

    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
