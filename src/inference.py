import sys
from ultralytics import YOLO

def inference_model(path_image: str) -> None:
    """
    Realiza inferência em uma imagem usando um modelo YOLO pré-treinado.
    """
    model = YOLO('../../runs/classify/train/weights/best.pt')
    pred = model.predict(path_image)
    print(pred)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    inference_model(image_path)
