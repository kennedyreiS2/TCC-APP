import sys
from ultralytics import YOLO

def inference_model(path_image) -> None:

    # load a custom trained model
    model = YOLO('../../runs/classify/train/weights/best.pt')

    pred = model.predict(path_image)

    print(pred)

if __name__ == "__main__":

    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    # Get the image path from the command-line argument
    image_path = sys.argv[1]

    # Call inference_model with the provided image path
    inference_model(image_path)
