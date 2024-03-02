from ultralytics import YOLO

def train_model() -> None:
    """
    Treina um modelo YOLO.
    """
    model = YOLO('yolov8n-cls.pt')

    model.train(data='../data/Classificacao-de-imagens-1', epochs=2, imgsz=32)

if __name__ == "__main__":
    train_model()
