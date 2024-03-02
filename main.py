import cv2
import os
import time
import keyboard
from ultralytics import YOLO
from src.text2audio import Text2Audio
from src.models import moondream_description, gemini_translater, gemini_ocr

def main():
    model = YOLO('./src/runs/classify/train/weights/best.pt')
    save_dir = './data/images'
    os.makedirs(save_dir, exist_ok=True)

    def exit_program():
        print("Programa finalizado.")
        cv2.destroyAllWindows()
        exit()

    while True:

        inp = input('Digite "s" para tirar uma foto, "q" para sair: ')

        if inp == "s":
            print("Tirando foto...")
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                print("Error: Could not open webcam.")
                exit()

            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            ret, frame = cap.read()

            if ret:
                current_time = int(time.time())
                print("Salvando foto...")
                image_filename = f'{save_dir}/image_{current_time}.jpg'
                cv2.imwrite(image_filename, frame)
                saved_image = cv2.imread(image_filename)
                results = model(saved_image)
                annotated_frame = results[0].plot()
                print(f'Result: {results[0].probs.top1}')

                annotated_image_filename = f'{save_dir}/annotated_image_{current_time}.jpg'
                cv2.imwrite(annotated_image_filename, annotated_frame)

                # names: {0: 'document', 1: 'scene'}
                if results[0].probs.top1 == 0:
                    text = gemini_ocr(image_path=image_filename)
                else:
                    text = gemini_translater(moondream_description(image_path=image_filename))

                print(text)

                if text:
                    conv = Text2Audio()
                    conv.text_to_audio(text=text, name_audio=f'audio.mp3')

            cap.release()
            cv2.destroyAllWindows()

        elif inp == "q":
            exit_program()

if __name__ == "__main__":
    main()
