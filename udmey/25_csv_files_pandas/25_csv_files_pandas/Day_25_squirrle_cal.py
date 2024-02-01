import pandas as pd


squirrel_df = pd.read_csv("Day_25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#count squirrel as per color i.e. group by color
print(squirrel_df.groupby(["Primary Fur Color"]).count())

#                      X     Y  ...  Other Interactions  Lat/Long
#Primary Fur Color              ...                              
#Black               103   103  ...                   8       103
#Cinnamon            392   392  ...                  33       392
#Gray               2473  2473  ...                 196      2473

# We need to create file of this result so lets do it in diffferent way


squirrel_df = pd.read_csv("Day_25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(squirrel_df[squirrel_df["Primary Fur Color"]== "Gray"])
red_squirrel_count = len(squirrel_df[squirrel_df["Primary Fur Color"]== "Cinnamon"])
black_squirrel_count = len(squirrel_df[squirrel_df["Primary Fur Color"]== "Black"])

print(f' gray squirrel :{gray_squirrel_count}')
print(f' red squirrel :{red_squirrel_count}')
print(f' Black squirrel :{black_squirrel_count}')


data_dict = {"Fur color" : ["Gray","Cinnamon","Black"],
             "Count": [gray_squirrel_count,red_squirrel_count,black_squirrel_count]
             }
#bring dictitonary to DataFrame and generate csv file
df =pd.DataFrame(data_dict)
print(df)

df.to_csv("25_squirrel_count.csv")
             
