import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\kennedy.reis\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class TesseractOCR:
    def get_text(self, img_path):
        img = cv2.imread(img_path)
        grayscale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        config_pytesseract = '--tessdata-dir ./src/tessdata'
        text = pytesseract.image_to_string(grayscale_image, lang='por',config=config_pytesseract)

        return text
