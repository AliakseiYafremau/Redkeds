# set_environment.ps1

# Проверяем существование .env файла
if (-Not (Test-Path .env)) {
    Write-Error ".env file not found in current directory" -ForegroundColor Red
    exit 1
}

# Читаем и устанавливаем переменные из .env файла
foreach($line in Get-Content .env) {
    # Пропускаем пустые строки и комментарии
    if ($line -match '^\s*#') { continue }
    if ($line -match '^\s*$') { continue }

    # Разбираем строки вида VARIABLE=value
    if ($line -match '^\s*([^#=]+?)\s*=\s*(.*)\s*$') {
        $varName = $matches[1].Trim()
        $varValue = $matches[2].Trim()

        # Удаляем кавычки если они есть
        $varValue = $varValue -replace '^["'']|["'']$', ''

        # Устанавливаем переменную окружения
        [System.Environment]::SetEnvironmentVariable($varName, $varValue)
        Write-Host "Set variable: $varName" -ForegroundColor DarkGray
    }
}

Write-Host "Environment variables loaded from .env file" -ForegroundColor Green