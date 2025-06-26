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
