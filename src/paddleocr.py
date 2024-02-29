from paddleocr import PaddleOCR
import os
import numpy as np
import cv2

# Configuração do modelo
ocr_model = PaddleOCR(lang='pt')

def extract_text_from_image(image_path):
    # Carrega a imagem usando o caminho fornecido
    image = cv2.imread(image_path)

    # Executa a detecção de texto na imagem
    result = ocr_model.ocr(image)

    if result is None or not any(result):
        return []

    # Inicializa um array para armazenar o texto extraído
    text_array = []

    # Itera sobre os resultados e extrai o texto
    for line in result[0]:
        text = line[1][0]  # Extrai o texto da linha
        text_array.append(text)  # Adiciona o texto ao array

    return text_array
