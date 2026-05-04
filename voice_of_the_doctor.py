import os
import time
from dotenv import load_dotenv
from gtts import gTTS
from elevenlabs.client import ElevenLabs

load_dotenv()



ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
DEBUG_MODE = True


def wait_for_file_ready(file_path):
    if not os.path.exists(file_path):
        while not os.path.exists(file_path):
            time.sleep(0.1)

    size1 = -1
    size2 = os.path.getsize(file_path)

    while size1 != size2:
        size1 = size2
        time.sleep(0.2)
        size2 = os.path.getsize(file_path)


def tts_gtts(text, file_path):
    try:
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save(file_path)

        wait_for_file_ready(file_path)

        print("gTTS saved:", file_path)

    except Exception as e:
        print("gTTS failed:", e)


def tts_elevenlabs(text, file_path):
    if not ELEVENLABS_API_KEY:
        raise Exception("ELEVENLABS_API_KEY missing in .env")

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio_stream = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",
        model_id="eleven_turbo_v2",
        text=text
    )

    with open(file_path, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    wait_for_file_ready(file_path)

    print("ElevenLabs saved:", file_path)


def smart_tts(text, output_name="output.mp3"):
    eleven_path = "elevenlabs_" + output_name
    gtts_path = "gtts_" + output_name

    try:
        tts_elevenlabs(text, eleven_path)

        if DEBUG_MODE:
            tts_gtts(text, gtts_path)

        return eleven_path

    except Exception as e:
        print("ElevenLabs failed:", e)
        print("Switching to gTTS fallback...")

        tts_gtts(text, gtts_path)
        return gtts_path


text = "Hello, I am your AI Doctor assistant working correctly."

final_file = smart_tts(text, "doctor_voice.mp3")

print("Final audio file used:", final_file)
