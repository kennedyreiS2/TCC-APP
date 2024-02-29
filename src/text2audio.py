import gtts
import os
from pathlib import Path
import pygame

class Text2Audio:
    # Function to convert text to audio
    def text_to_audio(self, text='deu bom', name_audio='output.mp3', language='pt'):
        output_directory = '/data/audio/'  # Diretório de saída
        output_path = os.path.join(output_directory, name_audio)  # Caminho completo para o arquivo de saída

        # Verifica se o diretório de saída existe, se não, cria
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Inicializa o mixer do pygame
        pygame.mixer.init()
        # Carrega o arquivo de áudio
        pygame.mixer.music.load(output_path)
        # Reproduz o áudio
        pygame.mixer.music.play()
        # Aguarda o término da reprodução
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
