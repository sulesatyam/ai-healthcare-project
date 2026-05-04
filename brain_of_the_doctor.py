import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_image_with_query(query, encoded_image, model):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise Exception("GROQ_API_KEY missing")

    client = Groq(api_key=api_key)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}"
                    },
                },
            ],
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    return response.choices[0].message.content