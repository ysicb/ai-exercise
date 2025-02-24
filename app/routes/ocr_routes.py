from fastapi import APIRouter, File, UploadFile
import yocr
from PIL import Image
import io

router = APIRouter()

@router.post("/ocr")
async def perform_ocr(file: UploadFile = File(...)):
    try:
        # Read image file
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Apply OCR using yocr
        extracted_text = yocr.ocr(image)

        return {"filename": file.filename, "text": extracted_text}

    except Exception as e:
        return {"error": str(e)}
