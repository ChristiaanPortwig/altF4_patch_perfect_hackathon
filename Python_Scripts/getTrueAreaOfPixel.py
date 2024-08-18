import cv2
import numpy as np

#The actual width of the measuring stick in mm
ACTUALWIDTH = 30

#TODO: Change fixed value about actual width of stick!!!!
def getTrueAreaOfPixel(image):
    """
    A function to find the true area represented by a single pixel from an image
s
    Params:
        Image: The image containing the measuring stick
    
    Returns:
        The area in mm^2 represented by one pixel.
        -1 If the area could not be found
    """
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Split the HSV channels
    h, s, v = cv2.split(hsv)

    # Normalize the Value channel
    v_normalized = cv2.normalize(v, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Merge the channels back
    hsv = cv2.merge([h, s, v_normalized])

    # Define the red color range
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for both red ranges
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine the masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Optional: Apply some morphological operations to clean up the mask
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate centroids of all contours
    centroids = []
    for cnt in contours:
        M = cv2.moments(cnt)
        if M['m00'] != 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            centroids.append((cx, cy))

    # Find the center of the image
    image_center = (image.shape[1] // 2, image.shape[0] // 2)

    pixel_count = 0

    # Find the centroid closest to the center of the image
    if centroids:
        distances = [np.linalg.norm(np.array(image_center) - np.array(c)) for c in centroids]
        closest_centroid = centroids[np.argmin(distances)]

        # Find the contour corresponding to the closest centroid
        closest_contour = contours[np.argmin(distances)]

        # Draw rotated bounding box around the closest contour
        rect = cv2.minAreaRect(closest_contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # Draw only the shorter edges and count pixels
        pixel_count = 0
        for i in range(4):
            pt1 = box[i]
            pt2 = box[(i + 1) % 4]
            edge_length = np.linalg.norm(pt1 - pt2)
            if edge_length < rect[1][0] or edge_length < rect[1][1]:
                cv2.line(image, tuple(pt1), tuple(pt2), (255, 255, 255), 2)
                pixel_count += int(edge_length)

    print("Change constant value for stick width!!!!")
    if(pixel_count!= 0):
        return (ACTUALWIDTH ** 2) / (pixel_count ** 2)
    else:
        return -1

if(__name__ == "__main__"):
    # Example usage
    image = cv2.imread('p147.jpg')
    print(getTrueAreaOfPixel(image))
