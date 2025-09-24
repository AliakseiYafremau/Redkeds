# Redkeds

Social network for designers to share their works and collaborate.

- 📔 Customizable profile
- 👍 Likes
- 🧑‍🤝‍🧑 Connections
- ✉️ Chat

## Installation and usage

### Requirements
- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installation

```bash
uv sync
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

### Apply migrations
```bash
alembic upgrade head
```

### Run the app
```bash
run
```

### Testing and linting

Additionaly, you can test, lint and format you code. All necessary dependencies should be installed.

```bash
uv sync --all-groups
```

To test the project, use `pytest`
```bash
pytest
```

To lint and format the code, use `ruff`
```bash
ruff format
ruff check
```
