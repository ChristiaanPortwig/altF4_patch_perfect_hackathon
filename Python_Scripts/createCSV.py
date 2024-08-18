import os 
from detectAndCrop import detect_and_crop
from getTrueAreaOfPixel import getTrueAreaOfPixel
from michaelScriptMockup import getPixels
import pandas as pd

PATH = "training/train_images"

df = pd.DataFrame({
    "Pothole number": [],
    "area": []
})

i = 1

for file in os.listdir(PATH):
    imageSource = f"{PATH}/{file}"

    # TODO: Use Michael's YOLO model in detect_and_crop, also work on training a better model!!!!
    stick, pothole = detect_and_crop(imageSource)

    # TODO: Change fixed value about actual width of stick!!!!
    areaOfPixel = getTrueAreaOfPixel(stick)

    pixelsInPothole = getPixels(pothole)

    truePotholeArea = areaOfPixel * pixelsInPothole

    df = pd.concat([df, pd.DataFrame({
        "Pothole number": [file.replace(".jpg","").replace("p","")],
        "area": [truePotholeArea]
    })], ignore_index=True)
    
    print(f"Appended num: {i}")
    i += 1

df.to_csv("areaAdded.csv", index=False)
