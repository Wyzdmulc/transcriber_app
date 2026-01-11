# Whisper Flask Transcriber 🎙️

A simple web app built with **Flask** and **OpenAI Whisper** that lets you:
- Upload audio files (`.wav`, `.mp3`, etc.) for transcription
- Record directly from your microphone in the browser
- Download the transcript as a Word (`.docx`) file
- Enjoy a clean interface with progress bar, recording animation, and success popup

---

## 🚀 Features
- Offline transcription using Whisper (no internet data usage)
- Supports multiple audio formats
- Real‑time recording in browser
- Progress bar + spinner + success popup for smooth UX
- Word document export

---

## 📂 Project Structure
    
    transcriber_app/ 
    ├── app.py              # Flask backend 
    ├── templates/ 
    │   └── index.html      # Frontend UI 
    ├── static/ 
    │   └── style.css       # Styling 
    ├── uploads/            # Temporary audio + transcripts 
    ├── requirements.txt    # Dependencies 
    ├── .gitignore          # Ignore venv/uploads 
    └── README.md           # Documentation


---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/whisper-transcriber.git
   cd whisper-transcriber

 2. **create virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate # Linux/macOS

3. **Python dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the app**
   ```bash
   python app.py
   
5. - Open browser → http://127.0.0.1:5000

## 📦Requirements
- Python 3.9+
- Flask
- openai-whisper
- python-docx
- ffmpeg (installed system‑wide

## 🌐 Deployment (Render Example)
1. **Add a Procfile:**
    ```bash
    web: gunicorn app:app
2. **Install Gunicorn:**
    ```bash
    pip install gunicorn
    pip freeze > requirements.txt
3. **Push to GitHub, then connect repo to Render.**
  - Build Command:
    ``` bash
    pip install -r requirements.txt

  - Start Command:
     ```bash
    gunicorn app:app
  Render will give you a live URL.

## Notes
- Whisper model size can be changed (tiny, base, small, medium, large) in app.py.
- Larger models = more accuracy but slower and heavier.
- Keep uploads/ out of GitHub (already in .gitignore).

## 📦 `requirements.txt`
    flask
    openai-whisper
    python-docx
    gunicorn

## .gitignore
  ```txt
venv/
__pycache__/
uploads/
*.pyc
