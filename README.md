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
```
```bash
  .\venv\Scripts\activate # для Windows
```

Укажите переменные окружения в `.env` (пример в .env.example)

Загрузите переменные окружения
```bash
  source ./scripts/set_environment.sh # для Linux/macOS
```
```bash
  .\scripts\set_environment.ps1 # для Windows
```

Включите режим разработки
```bash
  uv pip install -e .
```

## Применение миграций
```bash
  alembic upgrade head
```

## Запуск
Вы можете протестировать программу, запустив ее с помощью следующей команды
```bash
  run
```

## Тестирование

Запустите тестовую базу данных (проверьте корректность `.env`)
```bash
  docker compose -f docker-compose.yml up -d --build
```

Примените миграции к базе данных
```bash
  alembic upgrade head
```
