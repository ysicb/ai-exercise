import openai
import base64
from app.config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT

openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT

def analyze_image_with_gpt(image_bytes: bytes):
    """
    Sends an image to GPT-4o for analysis and extracts a summary.
    """
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Analyze the image and generate a summary in 5 words or less."},
            {"role": "user", "content": encoded_image}
        ]
    )

    summary_text = response["choices"][0]["message"]["content"]
    word_count = len(summary_text.split())

    return {"summary": summary_text, "number_of_words": word_count}
