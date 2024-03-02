from paddleocr import PaddleOCR
import cv2

ocr_model = PaddleOCR(lang='pt')

def extract_text_from_image(image_path: str):
    """
    Extrai texto de uma imagem usando o modelo OCR da PaddleOCR.
    """
    image = cv2.imread(image_path)
    result = ocr_model.ocr(image)
    if result is None or not any(result):
        return []
    text_array = []
    for line in result[0]:
        text = line[1][0]
        text_array.append(text)
    return text_array
