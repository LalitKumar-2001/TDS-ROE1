from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pytesseract
from PIL import Image
import io
import re

app = FastAPI()

EMAIL = "21f1004874@ds.study.iitm.ac.in"

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    # Load the image from the request
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    # OCR: Extract text from the image
    text = pytesseract.image_to_string(image)

    # Look for the pattern: two 8-digit numbers with a multiplication sign in between
    match = re.search(r"(\d{8})\s*[*x×]\s*(\d{8})", text.replace('\n', ''))
    if not match:
        return JSONResponse({"error": "Multiplication task not found! Please use an 8-digit x 8-digit image."}, status_code=400)

    num1, num2 = int(match.group(1)), int(match.group(2))
    answer = num1 * num2

    return {"answer": answer, "email": EMAIL}
