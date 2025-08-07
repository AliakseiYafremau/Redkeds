Import-Module dotenv -ErrorAction SilentlyContinue

# Проверяем существование .env файла
if (-Not (Test-Path .env)) {
    Write-Error ".env file not found in current directory"
    exit 1
}

# Загружаем переменные из .env файла
dotenv .env

# Проверяем, что переменные загружены (опционально)
Write-Host "Environment variables loaded from .env file" -ForegroundColor Green