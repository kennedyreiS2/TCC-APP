import cv2
import pytesseract
import os
from pathlib import Path

base_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Tesseract-OCR')
tesseract_exe = Path(base_dir) / 'tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_exe

class TesseractOCR:
    """
    Classe para realizar OCR usando Tesseract.
    """
    def get_text(self, img_path: str) -> str:
        """
        Extrai texto de uma imagem usando Tesseract OCR.
        """
        img = cv2.imread(img_path)
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        config_pytesseract = '--tessdata-dir ./src/tessdata'
        text = pytesseract.image_to_string(grayscale_image, lang='por', config=config_pytesseract)
        return text
