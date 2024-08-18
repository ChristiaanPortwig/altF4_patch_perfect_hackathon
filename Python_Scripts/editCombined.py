import pandas as pd

df = pd.read_csv("combined.csv")

df = df[df["area"] >= 0]

df.to_csv("combined.csv")