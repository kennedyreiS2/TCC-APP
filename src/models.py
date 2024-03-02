import os
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image
from transformers import CodeGenTokenizerFast as Tokenizer

import google.generativeai as genai
from src.moondream.moondream import Moondream, detect_device
from src.paddleocr import extract_text_from_image

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model_vision = genai.GenerativeModel(model_name="gemini-pro-vision")
model = genai.GenerativeModel(model_name="gemini-pro")

def moondream_description(image_path, prompt="Describe the image"):
    """
    Utiliza o modelo Moondream para descrever uma imagem.
    """
    device, dtype = detect_device()
    model_id = "vikhyatk/moondream1"
    tokenizer = Tokenizer.from_pretrained(model_id)
    moondream = Moondream.from_pretrained(model_id).to(device=device, dtype=dtype)
    img = Image.open(image_path)
    image_embeds = moondream.encode_image(img)
    answer = moondream.answer_question(image_embeds, prompt, tokenizer)
    return answer

def gemini_translater(description):
    """
    Utiliza o modelo Gemini para traduzir uma descrição para o português.
    """
    response = model.generate_content(
        f"Traduza para o português este texto {description}"
        )
    answer = response.text
    return answer

def gemini_ocr(image_path):
    """
    Utiliza o modelo Gemini para realizar OCR em uma imagem.
    """
    feature = extract_text_from_image(image_path)
    prompt = f"Realize OCR na imagem e cruze as informações com os dados já extraídos: {feature}. Contextualize do que se trata a imagem."

    cookie_picture = {
        'mime_type': 'image/jpeg',
        'data': Path(image_path).read_bytes()
    }

    response = model_vision.generate_content(
        contents=[prompt, cookie_picture],
        stream=True,
    )

    response.resolve()
    return response.text
