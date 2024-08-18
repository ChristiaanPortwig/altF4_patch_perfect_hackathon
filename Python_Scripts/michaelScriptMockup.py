import cv2
import math

def getPixels(croppedImage):
    """
    Gets the amount of pixels representing the pothole from an image
    params:
        croppedImage: An image that has been croppend around the bouding box of the pothole
    returns:
        pixelAmount: The amount of pixels in the pothole
    """

    #TODO: Implement Michael's code to get a more accurate representation of the area of the pothole
    width, height, channels = croppedImage.shape

    area = math.pi * (width//2) * (height//2)

    return area