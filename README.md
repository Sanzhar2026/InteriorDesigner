
<<<<<<< HEAD

Transform any room with AI-powered interior design using Adobe Firefly.

## Features
- Upload any room photo
- Choose from 8 design styles
- Generate 4 stunning variations
- Download your favorite designs

## Tech Stack
- Next.js 14 (Frontend)
- FastAPI (Backend)
- Adobe Firefly API (AI Generation)
- Tailwind CSS (Styling)
=======
cat > README.md << 'EOF'
# 🏠 AI Interior Designer

**Generate interior design concepts using Stable Diffusion AI**

## 📸 Demo

Upload a photo of your room → choose a style → get 4 design variations

## ✨ Features

- 📷 Upload any room photo
- 🎨 8 design styles (Modern, Classic, Loft, Scandinavian, etc.)
- 🤖 AI-powered generation with Stable Diffusion
- 🖼️ 4 unique design variations per request
- 💾 Download your favorite design
- 🌙 Dark theme UI with glass-morphism effects

## 🛠 Tech Stack

- **Frontend**: Next.js 14, TypeScript, Tailwind CSS, Lucide Icons
- **Backend**: FastAPI, Python, Uvicorn
- **AI**: Stable Diffusion (Colab / Hugging Face / Local)
- **Deployment**: Vercel (Frontend), Railway (Backend)

## 🚀 Quick Start

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

cat > README.md << 'EOF'
# 🏠 AI Interior Designer

**Генерация дизайна интерьера через Stable Diffusion**

## 📸 Демо

Загрузи фото комнаты → выбери стиль → получи 4 варианта дизайна

## 🛠 Технологии

- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python
- **AI**: Stable Diffusion (Colab / Hugging Face)

## 🚀 Быстрый старт

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

---

## 🇰🇿 Қазақша нұсқасы

cat > README_KZ.md << 'EOF'
# 🏠 AI Interior Designer

**Stable Diffusion көмегімен интерьер дизайнын жасау**

## 📸 Демо

Бөлменің суретін жүкте → стильді таңда → 4 дизайн нұсқасын ал

## ✨ Мүмкіндіктер

- 📷 Кез келген бөлменің суретін жүктеу
- 🎨 8 дизайн стилі (Modern, Classic, Loft, Scandinavian т.б.)
- 🤖 Stable Diffusion көмегімен AI-генерация
- 🖼️ Бір сұранысқа 4 бірегей дизайн нұсқасы
- 💾 Ұнаған нұсқасын жүктеп алу
- 🌙 Шыны эффектілері бар қараңғы тақырып

## 🛠 Технологиялар

- **Фронтенд**: Next.js 14, TypeScript, Tailwind CSS, Lucide Icons
- **Бекенд**: FastAPI, Python, Uvicorn
- **AI**: Stable Diffusion (Colab / Hugging Face / Локалды)
- **Деплой**: Vercel (Фронтенд), Railway (Бекенд)

## 🚀 Жылдам бастау

### Бекенд
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```
>>>>>>> 614d2e738dddddde6625b6ef894366f581db3de2

🇬🇧 ENGLISH

📋 Colab + ngrok Setup Instructions

Step 1: Open Google Colab

Go to https://colab.research.google.com/
Click "New Notebook"
Name it: Stable Diffusion API
Step 2: Enable GPU

Click Runtime → Change runtime type
Select "T4 GPU"
Click "Save"
Step 3: Copy the Code

Copy the entire code from backend/colab_stable_diffusion.ipynb and paste it into the Colab notebook.

Step 4: Get ngrok Token

Go to https://ngrok.com
Sign up / Log in
Go to "Your Authtoken"
Copy your token (looks like: 2uJZ2w7DBvS8Xk5HxJ9YrM1NqL3TzP4Q)
Replace ngrok_token = "YOUR_TOKEN_HERE" in the code
Step 5: Run the Notebook

Click Runtime → Run all (or Ctrl+F9)
Wait 2-3 minutes for the model to download
Copy the public URL shown at the end
Step 6: Update Your Backend

bash
cd /Users/iliaszhymabaev/Desktop/Freelance/InteriorDesigner/backend
echo "SD_API_URL=https://your-ngrok-url.ngrok-free.app" >> .env
🇷🇺 РУССКИЙ

📋 Инструкция по настройке Colab + ngrok

Шаг 1: Открой Google Colab

Перейди на https://colab.research.google.com/
Нажми "Новый блокнот"
Назови его: Stable Diffusion API
Шаг 2: Включи GPU

Нажми Runtime → Change runtime type
Выбери "T4 GPU"
Нажми "Сохранить"
Шаг 3: Скопируй код

Скопируй весь код из backend/colab_stable_diffusion.ipynb и вставь в блокнот Colab.

Шаг 4: Получи токен ngrok

Перейди на https://ngrok.com
Зарегистрируйся / Войди
Перейди в "Your Authtoken"
Скопируй свой токен (выглядит как: 2uJZ2w7DBvS8Xk5HxJ9YrM1NqL3TzP4Q)
Замени ngrok_token = "ВАШ_ТОКЕН_ЗДЕСЬ" в коде
Шаг 5: Запусти блокнот

Нажми Runtime → Run all (или Ctrl+F9)
Подожди 2-3 минуты, пока загрузится модель
Скопируй публичный URL, который появится в конце
Шаг 6: Обнови бекенд

bash
cd /Users/iliaszhymabaev/Desktop/Freelance/InteriorDesigner/backend
echo "SD_API_URL=https://ваш-ngrok-url.ngrok-free.app" >> .env
🇰🇿 ҚАЗАҚША

📋 Colab + ngrok орнату нұсқаулығы

1-қадам: Google Colab-ты ашу

https://colab.research.google.com/ сайтына өт
"Жаңа блокнот" бас
Атын жаз: Stable Diffusion API
2-қадам: GPU-ны қосу

Runtime → Change runtime type бас
"T4 GPU" таңда
"Сақтау" бас
3-қадам: Кодты көшіру

backend/colab_stable_diffusion.ipynb файлындағы барлық кодты көшіріп, Colab блокнотына қой.

4-қадам: ngrok токенін алу

https://ngrok.com сайтына өт
Тіркел / Кір
"Your Authtoken" бөліміне өт
Токеніңді көшір (мысалы: 2uJZ2w7DBvS8Xk5HxJ9YrM1NqL3TzP4Q)
Кодтағы ngrok_token = "СЕНІҢ_ТОКЕНІҢ" деген жерге қой
5-қадам: Блокнотты іске қосу

Runtime → Run all бас (немесе Ctrl+F9)
Модель жүктелгенше 2-3 минут күт
Соңында шыққан публикалық URL-ды көшір
6-қадам: Бекендті жаңарту

bash
cd /Users/iliaszhymabaev/Desktop/Freelance/InteriorDesigner/backend
echo "SD_API_URL=https://сенің-ngrok-url.ngrok-free.app" >> .env
📝 Важно / Important / Маңызды

🇬🇧	🇷🇺	🇰🇿
Colab session lasts ~12 hours	Сессия Colab длится ~12 часов	Colab сессиясы ~12 сағатқа созылады
ngrok URL changes on each restart	ngrok URL меняется при каждом перезапуске	ngrok URL әр қайта іске қосқанда өзгереді
Update .env with new URL after restart	Обновляй .env новым URL после перезапуска	Қайта іске қосқаннан кейін .env-ді жаңа URL-мен жаңарт
Keep the Colab tab open	Держи вкладку Colab открытой	Colab қойындысын ашық ұста
