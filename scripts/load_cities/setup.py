import argparse
import asyncio
import logging
from uuid import uuid4

import asyncpg
import openpyxl

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def load_xlsx(filename: str) -> list:
    """Загружает xlsx файл."""
    return [
        cell.value
        for cell in openpyxl.load_workbook(filename).active["A"]
        if cell.value is not None
    ]


async def load_data(
    filename: str, host: str, port: int, user: str, database: str, password: str
) -> None:
    """Загружает данные в базу данных."""
    connection = await asyncpg.connect(
        host=host,
        port=port,
        user=user,
        database=database,
        password=password,
    )
    try:
        data = load_xlsx(filename)
        for i in range(len(data)):
            data[i] = (uuid4(), data[i])
        await connection.executemany(
            "INSERT INTO cities (id, name) VALUES ($1, $2)",
            data,
        )
    finally:
        await connection.close()


async def main() -> None:
    """Функция для запуска скрипта."""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=5432)
    parser.add_argument("--user", type=str, default="postgres")
    parser.add_argument("--database", type=str, default="postgres")
    parser.add_argument("--password", type=str, default="1234")

    arguments = parser.parse_args()
    await load_data(
        filename=arguments.filename,
        host=arguments.host,
        port=arguments.port,
        user=arguments.user,
        database=arguments.database,
        password=arguments.password,
    )


if __name__ == "__main__":
    asyncio.run(main())
