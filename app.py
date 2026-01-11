from flask import Flask, render_template, request, send_file
import whisper
from docx import Document
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load Whisper model (choose: tiny, base, small, medium, large)
model = whisper.load_model("base")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files["audio"]
    filepath = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(filepath)

    # Transcribe with Whisper
    result = model.transcribe(filepath)
    text = result["text"]

    # Save to Word file
    output_path = os.path.join(UPLOAD_FOLDER, "transcription.docx")
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
