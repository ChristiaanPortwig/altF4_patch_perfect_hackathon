library("tidyverse")
combined <- read.csv("C:/Users/chris/OneDrive/1.Personal/0.ProjekteWerk/Patch perfect hackathon/patchPerfectPlay/Scripts/usable/combined.csv")

ggplot(data = combined) + geom_point(mapping = aes(x = area, y = Bags.used), color = "red")