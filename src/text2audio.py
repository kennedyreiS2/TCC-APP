import gtts
from playsound import playsound
import os

class Text2Audio:
    # Function to convert text to audio
    def text_to_audio(self, text='deu bom', name_audio='output.mp3', language='pt'):

        output_path = os.path.join(r'data/audio', name_audio)

        tts = gtts.gTTS(text, lang=language)
        tts.save(output_path)
        playsound(output_path)
