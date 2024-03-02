import os
import gtts
import pygame

class Text2Audio:
    """
    Classe para converter texto em áudio.
    """
    def text_to_audio(self, text='deu bom', name_audio='output.mp3', language='pt'):
        """
        Converte texto em áudio e reproduz o áudio.
        """
        output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio', name_audio)

        tts = gtts.gTTS(text, lang=language)
        tts.save(output_path)

        pygame.mixer.init()
        pygame.mixer.music.load(output_path)
        pygame.mixer.music.play()

        # Espera até que a música termine de tocar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Fecha a instância do pygame.mixer
        pygame.mixer.quit()

if __name__ == "__main__":
    conv = Text2Audio()
    conv.text_to_audio(text='Olá, mundo!', name_audio='hello_world.mp3')
