# AI Doctor (Voice + Vision)

An intelligent AI-powered doctor assistant that can:

* Listen to patient voice (speech input)
* Understand symptoms using AI
* Analyze medical images
* Respond with realistic doctor voice

---

## Features

* **Speech-to-Text (STT)** using Groq Whisper
* **AI Diagnosis** using LLM (LLaMA model)
* **Image Analysis** (medical image understanding)
* **Text-to-Speech (TTS)** using:

  * ElevenLabs (primary)
  * gTTS (fallback)
* **Gradio Web Interface**

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd AI-DOCTOR
```

### 2. Install dependencies (Pipenv)

```bash
pipenv install
pipenv shell
```

OR using pip:

```bash
pip install groq speechrecognition pydub gradio python-dotenv gtts elevenlabs
```

---

## Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

---

## Run the Application

```bash
python gradio_app.py
```

Then open:

```
http://127.0.0.1:7860
```

---

## How It Works

### Step 1: Voice Input

* User speaks through microphone
* Audio recorded using `speech_recognition`

### Step 2: Transcription

* Audio converted to text using Groq Whisper model

### Step 3: AI Processing

* Text and image sent to LLM (LLaMA)
* Model generates medical response

### Step 4: Voice Output

* Response converted to speech using ElevenLabs or gTTS

---

## Tech Stack

* Python 3.11
* Gradio (UI)
* Groq API (LLM + Whisper)
* SpeechRecognition
* Pydub
* ElevenLabs API
* gTTS

---

## Requirements

### Audio Dependencies

* Install **ffmpeg**
* Install **portaudio**

For Windows:

```bash
pip install pipwin
pipwin install pyaudio
```

---

## Test Scripts

### Test Groq

```bash
python test_groq.py
```

### Test Gradio

```bash
python tes_groq.py
```

---

## Future Improvements

* Add patient history memory (RAG)
* Improve UI/UX
* Add multilingual support
* Deploy on cloud (Streamlit / HuggingFace Spaces)

---

## Author

Satyam Sule

B.Tech Data Science & Bioinformatics

Email: sulesatyam68@gmail.com

LinkedIn: www.linkedin.com/in/satyamsule

