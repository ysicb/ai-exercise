from fastapi import APIRouter, File, UploadFile, HTTPException
import openai
from app.schemas import ImageSummaryResponse
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import io,os,base64

load_dotenv()

router = APIRouter()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

@router.post("/image-summary", response_model=ImageSummaryResponse)
async def summarize_image(file: UploadFile = File(...)):
    if not OPENAI_API_KEY:
        raise HTTPException(status_code=500, detail="OpenAI API key is missing")

    image = Image.open(io.BytesIO(await file.read()))
    image_bytes = await file.read()
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Describe the image briefly in less than 5 words."},
                {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is in this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            },
            ],
            max_tokens=50  # Keep response short
        )
 
        description = response.choices[0].message.content
        number_of_words = len(description.split())
 
   
 
        return ImageSummaryResponse(summary=description, number_of_words=number_of_words)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))