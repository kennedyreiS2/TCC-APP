import cv2
from ultralytics import YOLO
import time
import os
import keyboard
from src.tesseract_ocr import TesseractOCR
from src.text2audio import Text2Audio

# Load the YOLOv8 model
model = YOLO('./src/runs/classify/train/weights/best.pt')

# Set the save directory for images
save_dir = './data/images'

# Create the directory if it does not exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Open the video capture (webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Variable to store the time of the last photo capture
last_capture_time = time.time()

# Loop through the video frames in real-time
while True:
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Display the frame
        cv2.imshow("Webcam", frame)

        # Check if one minute has passed since the last photo capture
        current_time = time.time()
        if current_time - last_capture_time >= 10:
            # Save the frame as an image
            image_filename = f'{save_dir}/image_{int(current_time)}.jpg'
            cv2.imwrite(image_filename, frame)

            # Run YOLOv8 inference on the saved image
            saved_image = cv2.imread(image_filename)
            results = model(saved_image)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Check if the image is classified as "document"
            if results[0].names[0] == "document":
                # Perform OCR using Tesseract on the saved image
                ocr = TesseractOCR()
                text = ocr.get_text(image_filename)
                print("Text:", text)
                if text:
                    conv = Text2Audio()
                    conv.text_to_audio(text=text)

            # Display the annotated frame
            cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Update the last capture time
            last_capture_time = current_time

        # Check for the Ctrl + x key combination to exit the loop
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('x'):
            break

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
