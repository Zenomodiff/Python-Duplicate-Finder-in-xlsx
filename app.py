import pandas as pd

data = pd.read_excel('output_file.xlsx')

data.drop_duplicates(subset = "Channel Name", keep ="first", inplace = True)

df = data

df.to_csv("master.csv")




