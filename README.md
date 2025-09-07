# Installation and usage

## Requirements
- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

```bash
uv sync --all-groups
```

Activate virtual environment
```bash
source .venv/bin/activate # for Linux/macOS
```
```bash
.\venv\Scripts\activate # for Windows
```

Specify environment variables in `.env` (example in .env.example)

Load environment variables
```bash
source set_environment.sh # for Linux/macOS
```

Install development tools
```bash
uv pip install -e .
```

## Apply migrations
```bash
alembic upgrade head
```

## Run the app
```bash
run
```