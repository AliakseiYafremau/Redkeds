# Установка и использование

## Требования
- Python 3.11 или выше
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Установка

Обновите зависимости проекта
```bash
uv sync
```

Активируйте виртуальное окружение
```bash
source .venv/bin/activate # для Linux/macOS
.\venv\Scripts\activate # для Windows
```

Загрузите переменные окружения
```bash
source ./scripts/set_environment.sh
```

Включите режим разработки
```bash
uv pip install -e .
```

## Запуск
Вы можете протестировать программу, запустив ее с помощью следующей команды
```bash
app # Команда ничего не выведет
```

## Миграции Alembic

- Миграции хранятся в src/app/adapters/migrations/versions
- Конфиг: src/app/adapters/alembic.ini
- Асинхронный режим (см. env.py)
- Для автогенерации схемы используется Base из src/app/adapters/models.py
- Не забудь добавить в .env DATABASE_URL

### Примеры команд

- Создать миграцию:
  alembic -c src/app/adapters/alembic.ini revision --autogenerate -m "your message"
- Применить миграции:
  alembic -c src/app/adapters/alembic.ini upgrade head
- Откатить миграцию:
  alembic -c src/app/adapters/alembic.ini downgrade -1
