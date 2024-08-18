import os 
from detectAndCrop import detect_and_crop
from getTrueAreaOfPixel import getTrueAreaOfPixel
from michaelScriptMockup import getPixels
import pandas as pd
import math
import joblib
import numpy as np


PATH = "C:/Users/mgshe/Documents/altF4_patch_perfect_hackathon/Python_Scripts/images"

# Replace 'mlp_model.pkl' with the path to your saved model
model = joblib.load('C:/Users/mgshe/Documents/altF4_patch_perfect_hackathon/Models/svr_model.pkl')


df = pd.DataFrame({
    "Pothole number": [],
    "Bags used": []
})

i = 1

for file in os.listdir(PATH):
    imageSource = f"{PATH}/{file}"

    stick, pothole = detect_and_crop(imageSource)

    areaOfPixel = getTrueAreaOfPixel(stick)

    pixelsInPothole = getPixels(pothole)

    truePotholeArea = areaOfPixel * pixelsInPothole

    # Predict the output using the model
    predicted_value = model.predict([[truePotholeArea]])
    p = abs(predicted_value[0])

    df = pd.concat([df, pd.DataFrame({
        "Pothole number": [file.replace(".jpg","").replace("p","")],
        "Bags used": p
    })], ignore_index=True)
    
    print(f"Appended num: {i}")
    i += 1

df.to_csv("testingfinal.csv", index=False)
