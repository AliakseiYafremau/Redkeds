FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"


WORKDIR /app

COPY . /app/
RUN uv sync --locked
ENV PATH="/app/.venv/bin:$PATH"


CMD [ "python3", "-m", "uvicorn", "src.app.main:get_app", "--host=0.0.0.0", "--port=8000" ]