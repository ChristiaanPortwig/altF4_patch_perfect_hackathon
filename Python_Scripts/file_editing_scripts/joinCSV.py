import pandas

BAGSUSEDPATH = "C:/Users/mgshe/Documents/altF4_patch_perfect_hackathon/CSV_Files/train_labels.csv"
AREAPATH = "C:/Users/mgshe/Documents/altF4_patch_perfect_hackathon/CSV_Files/areaAdded.csv"

#Converts csv files to dataframes
bags_df = pandas.read_csv(BAGSUSEDPATH)
area_df = pandas.read_csv(AREAPATH)

#merges data frames
merged_df = pandas.merge(bags_df, area_df, left_on="Pothole number", right_on="Pothole number", how="inner")

#Converts back to csv
merged_df.to_csv("./combined.csv")