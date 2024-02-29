import google.generativeai as genai
from pathlib import Path
from dotenv import load_dotenv
import os
from IPython.display import Markdown
import textwrap

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro-vision')

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def describe_environment(image_path, prompt, mime_type):

    cookie_picture = {
        'mime_type': mime_type,
        'data': Path(image_path).read_bytes()
    }

    response = model.generate_content(
        contents=[prompt, cookie_picture],
        stream=True
    )

    response.resolve()
    return response.text
