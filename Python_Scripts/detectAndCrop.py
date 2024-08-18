import cv2
from ultralytics import YOLO

def detect_and_crop(image_path):
    """
    Detects different objects in a pothole image and crops the image accordingly

    params:
        image_path: The path where the image is stored
    
    returns:
        [croppedImageOfStick, croppedImageOfPothole]
    """
    # Load the image
    image = cv2.imread(image_path)

    # Load the YOLOv8 model
    model = YOLO('../../Models/potholeTrained.pt')  # You can use a different YOLOv8 model if needed

    # Detect objects in the image
    results = model(image)

    # Function to crop the image
    def crop_image(image, x1, y1, x2, y2):
        return image[y1:y2, x1:x2]

    # Initialize variables
    cropped_objects = []
    found_class_2 = None
    found_class_1 = None
    found_class_0 = None

    # Process detected objects
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Convert tensor to list
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])  # Convert to integers
            class_number = int(box.cls[0].item())  # Get the class number

            if class_number == 2 and found_class_2 is None:
                found_class_2 = crop_image(image, x1, y1, x2, y2)
            elif class_number == 1 and found_class_1 is None:
                found_class_1 = crop_image(image, x1, y1, x2, y2)
            elif class_number == 0 and found_class_0 is None:
                found_class_0 = crop_image(image, x1, y1, x2, y2)

    # Determine the return array based on conditions
    if (found_class_2 is not None or found_class_1 is not None) and found_class_0 is not None:
        cropped_objects.append(found_class_2 if found_class_2 is not None else found_class_1)
        cropped_objects.append(found_class_0)
    elif found_class_0 is not None:
        cropped_objects.append(found_class_0)
        cropped_objects.append(found_class_0)
    else:
        cropped_objects.append(image)
        cropped_objects.append(image)

    return cropped_objects

if(__name__ == "__main__"):
    # Example usage
    image_path = 'p147.jpg'
    cropped_images = detect_and_crop(image_path)
    for i, cropped_image in enumerate(cropped_images):
        cv2.imwrite(f'cropped_image_{i}.jpg', cropped_image)
