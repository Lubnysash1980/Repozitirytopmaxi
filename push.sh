#!/bin/bash

# 🔹 Піднімаємо ssh-agent і додаємо ключ
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# 🔹 Додаємо всі зміни (файли, що не в .gitignore)
git add .

# 🔹 Запит коментаря до коміту
read -p "Enter commit message: " msg
git commit -m "$msg" 2>/dev/null

# 🔹 Синхронізація з GitHub
git pull origin main --rebase

# 🔹 Пушимо на GitHub
git push -u origin main

echo "✅ Push complete!"
