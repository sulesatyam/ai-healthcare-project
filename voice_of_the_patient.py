import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)



def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            logging.info("Speak now...")
            audio_data = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

            logging.info("Recording complete.")

            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Saved to {file_path}")

    except Exception as e:
        logging.error(f"Error: {e}")



def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise Exception("GROQ_API_KEY not found in .env")

    client = Groq(api_key=api_key)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text



if __name__ == "__main__":
    audio_filepath = "patient_voice.mp3"

    record_audio(audio_filepath)

    text = transcribe_with_groq(audio_filepath)
    print("Transcription:", text)