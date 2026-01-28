# 1️⃣ Налаштовуємо Git (тільки один раз)
git config --global user.name "Lubnysash1980"
git config --global user.email "твій_справжній_email@github.com"

# 2️⃣ Створюємо README (якщо ще немає)
echo "# Repozitirytopmaxi" > README.md

# 3️⃣ Ініціалізуємо Git (якщо ще не робили)
git init

# 4️⃣ Додаємо файл до індексу
git add README.md

# 5️⃣ Робимо перший коміт
git commit -m "first commit"

# 6️⃣ Перейменовуємо гілку на main
git branch -M main

# 7️⃣ Додаємо віддалений репозиторій (SSH)
git remote add origin git@github.com:Lubnysash1980/Repozitirytopmaxi.git

# 8️⃣ Пушимо на GitHub
git push -u origin main
