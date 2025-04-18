# Sandra Voice Assistant 🎙️

Голосовой ассистент, который реагирует на ключевое слово **Sandra** и управляет Spotify по голосу. Проект будет дорабатываться и обновляться 🚧.

---

## 🚀 Возможности

- Реакция на голосовое ключевое слово "Sandra"
- Воспроизведение треков, переключение плейлистов, управление музыкой
- Поддержка команд: `play`, `stop`, `next`, `back`, `playlist`, `spotify`
- Аудио-отклики на пробуждение ассистента (в папке `pharse`)

Подробнее в [COMMANDS.md](./COMMANDS.md)

---

## 📦 Установка

### 1. Клонируй репозиторий и перейди  в папку
```bash
git clone https://github.com/Exslayder/spotify-voice-assistant.git
cd spotify-voice-assistant
```
### 2. Cоздай виртуальную среду
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
```

### 3. Установи зависимости
```bash
pip install -r requirements.txt
```

### 4. Настрой `.env` файл

Создай `.env` и добавь в него:

```env
SPOTIPY_CLIENT_ID=your_id
SPOTIPY_CLIENT_SECRET=your_secret
SPOTIPY_REDIRECT_URI=http://localhost:8080

PORCUPINE_KEY=your_porcupine_key
PORCUPINE_KEYWORD_PATH=your_path/wake_word/sandra.ppn
VOSK_MODEL_PATH=your_path/vosk/small-model-eng
AUDIO_RESPONSES_PATH=your_path/pharse
```

🟢 Получить Spotify ключи: https://developer.spotify.com/documentation/web-api/concepts/apps  
🟣 Получить Porcupine ключи: https://console.picovoice.ai/  
🔴 Видео-гайд по созданию своей фразы вместо `Sandra.ppn` : https://www.youtube.com/watch?v=T6jxYRSyF2w

---

## 📁 Модели

🟢 **Vosk**: Скачай модель по ссылке https://alphacephei.com/vosk/models  
  Мы используем `vosk-model-small-en-us-0.15`, но ты можешь выбрать любую подходящую
🟣 **Wake Word**: Создай `.ppn` через https://console.picovoice.ai/  
  Можешь использовать любую фразу. Наш wake word — "Sandra".

---

## ▶️ Запуск

```bash
python main.py
```

---

## 📢 Аудио-ответы

В папке `pharse` лежат 5 файлов-ответов. Можешь заменить их своими реакциями или доработать. Путь к ним прописывается в `.env` через `AUDIO_RESPONSES_PATH`.

---

## 🤝 Контакты
Если у тебя есть предложения, баги или хочешь поучаствовать — welcome!
Можешь написать мне.
