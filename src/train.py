from ultralytics import YOLO

def train_model() -> None:
    # Load a model
    model = YOLO('yolov8n-cls.pt')

    # Train the model
    model.train(data='../data/Classificacao-de-imagens-1', epochs=2, imgsz=32)

if __name__ == "__main__":
    train_model()
