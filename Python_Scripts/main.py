from detectAndCrop import detect_and_crop
from getTrueAreaOfPixel import getTrueAreaOfPixel
from michaelScriptMockup import getPixels

imageSource = "p147.jpg"

#TODO: Use michaels yolo model in detect_and_crop, also work on training a better model!!!!
stick, pothole = detect_and_crop(imageSource)

#TODO: Change fixed value about actual width of stick!!!!
areaOfPixel = getTrueAreaOfPixel(stick)

pixelsInPothole = getPixels(pothole)

truePotholeArea = areaOfPixel * pixelsInPothole

print(truePotholeArea)