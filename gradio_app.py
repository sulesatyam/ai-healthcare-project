import os
import gradio as gr
from dotenv import load_dotenv

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import smart_tts

load_dotenv()


system_prompt = """
You are a professional doctor.
Give short, clear medical advice in 1-2 sentences.
"""


def process_inputs(audio_filepath, image_filepath):

    # STEP 1: Speech → Text
    speech_text = transcribe_with_groq(audio_filepath)

    # STEP 2: Image + Text → Doctor response
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_text,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )
    else:
        doctor_response = "No image provided for analysis."

    # STEP 3: Text → Speech
    voice_file = smart_tts(doctor_response, "final.mp3")

    return speech_text, doctor_response, voice_file


iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Patient Speech"),
        gr.Textbox(label="Doctor Response"),
        gr.Audio(label="Doctor Voice", autoplay=True)  
    ],
    title="AI Doctor (Voice + Vision)"
)

iface.launch()