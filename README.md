# 🎬 AI Video Generator

An AI-powered cinematic video generation system built using **FastAPI**, **OpenRouter AI**, **MoviePy**, and **JavaScript frontend**.

This project generates:
- AI-written cinematic scripts
- AI-generated images
- AI voice narration
- Final rendered video automatically

---

# 🚀 Features

✅ AI Script Generation  
✅ AI Image Generation  
✅ AI Voice Narration  
✅ Automatic Video Rendering  
✅ FastAPI Backend  
✅ Modern Frontend UI  
✅ Downloadable Final Video  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| FastAPI | API Framework |
| OpenRouter API | AI Script Generation |
| MoviePy | Video Rendering |
| Pollinations AI | AI Image Generation |
| gTTS | Voice Generation |
| HTML/CSS/JavaScript | Frontend UI |
| Uvicorn | FastAPI Server |

---

# 📁 Project Structure

```bash
AI-video Generation/
│
├── backend/
│   ├── models/
│   │   └── request_models.py
│   │
│   ├── outputs/
│   │   ├── scene_1.png
│   │   ├── scene_2.png
│   │   ├── scene_3.png
│   │   ├── scene_4.png
│   │   ├── voice.mp3
│   │   └── final.mp4
│   │
│   ├── services/
│   │   ├── image_service.py
│   │   ├── script_service.py
│   │   ├── video_service.py
│   │   └── voice_service.py
│   │
│   ├── .env
│   ├── main.py
│   ├── requirements.txt
│   └── test_script.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-video-Generation.git
```

---

## 2️⃣ Navigate to Project

```bash
cd AI-video-Generation/backend
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file inside `backend/`

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# ▶️ Run FastAPI Server

Inside backend folder:

```bash
python -m uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

Swagger API Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 🌐 Run Frontend

Open:

```bash
frontend/index.html
```

using:
- VS Code Live Server
- or browser directly

Frontend runs on:

```bash
http://127.0.0.1:5500
```

---

# 🎥 How It Works

## Step 1
User enters cinematic prompt.

## Step 2
OpenRouter AI generates cinematic script.

## Step 3
Pollinations AI generates scene images.

## Step 4
Voice narration is generated using gTTS.

## Step 5
MoviePy combines:
- images
- narration
- scenes

into final cinematic video.

---

# 📸 Sample Prompt

```text
Create a cinematic motivational video about discipline and success
```

---

# 📦 Requirements

```txt
fastapi
uvicorn
python-dotenv
requests
moviepy
gtts
openai
pillow
imageio
imageio-ffmpeg
numpy
```

---

# 📌 Output

Generated files are stored inside:

```bash
backend/outputs/
```

Final video:

```bash
final.mp4
```

---

# 🔥 Future Improvements

- AI subtitle generation
- Background music
- Better AI image models
- User authentication
- Cloud deployment
- Database integration

---

# 👨‍💻 Author

**Joshuaraja**

Full Stack Developer | AI Enthusiast

---

# ⭐ GitHub

If you like this project, give it a ⭐ on GitHub!
