#!/bin/bash

# Запуск ssh-agent і завантаження ключа
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Додаємо всі зміни (файли, що не в .gitignore)
git add .

# Комітимо з повідомленням "Update project" (якщо є зміни)
git commit -m "Update project" 2>/dev/null

# Синхронізація з GitHub (pull --rebase)
git pull origin main --rebase

# Пушимо на GitHub
git push -u origin main
