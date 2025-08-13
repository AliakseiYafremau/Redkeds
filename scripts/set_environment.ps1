# Устанавливает переменные из .env (PowerShell)

if (-Not (Test-Path .env)) {
    Write-Error "ОШИБКА: Файл .env не найден" -ForegroundColor Red
    exit 1
}

foreach ($line in Get-Content .env) {
    if ($line -match '^\s*#') { continue }  # Пропускаем комментарии
    if ($line -match '^\s*$') { continue }  # Пропускаем пустые строки

    if ($line -match '^\s*([^=]+)\s*=\s*(.*)') {
        $name = $matches[1].Trim()
        $value = $matches[2].Trim() -replace '^["'']|["'']$', ''  # Удаляем кавычки в начале/конце
        Set-Item -Path "env:$name" -Value $value
    }
}

Write-Host "Переменные из .env загружены" -ForegroundColor Green