with open("weather_data_day25.csv") as weather_file:
    weather_days=weather_file.readlines() #this bring data as list
    for days in weather_days:
        weather_day = days.strip()  # removes \n from list records
        print(weather_day)

#Another way as per Udmey
print(" ")

import csv

temperatures = []
with open("weather_data_day25.csv") as weather_file:
    data = csv.reader(weather_file)
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
            
        
print(temperatures)


# easiest way to do is use pandas
import pandas as pd

weather_file_df = pd.read_csv("weather_data_day25.csv")
#print(weather_file_df.to_string)
print(weather_file_df)  # whole data is dataframe (df)
print(type(weather_file_df)) 
print(weather_file_df["temp"]) # to get just temperature as series


#converting this dataframe to dictionary
#days , temprature and condition as sub dicitonaries
print(weather_file_df.to_dict())

#getting temperature in list
temp_list =  weather_file_df["temp"].to_list()
print(temp_list)


# get average of temperature
avg_temp =  weather_file_df["temp"].mean()
print(f'avg_temp : {avg_temp}')



# MAX of temperature
max_temp =  weather_file_df["temp"].max()
print(f'max_temp : {max_temp}')

# another way to get temperature as list
print(weather_file_df.temp)

# check the maximum temperatur and get that row
print(weather_file_df[weather_file_df.temp == weather_file_df.temp.max()])

print(f'Weather is {weather_file_df[weather_file_df.temp == weather_file_df.temp.max()].condition} today')

#dicitionary to dataframe
data= {
        "cars" : ["MCDZ","JAG","LAM"],
        "cost" : [1.2  ,2.3  ,3.4]
}


myvar=pd.DataFrame(data)
print(myvar)

print("")
print("with indexes of our own instead of 0,1,2")
myvar_df=pd.DataFrame(data, index = ["a","b","c"]) # i have names the index as a,b and c
print(myvar_df)

#loading above dicitonary to csv file
myvar_df.to_csv("new_file_25.csv")


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

family_df = pd.DataFrame(myfamily)
print(family_df)
family_df.to_csv("new_file_25_1.csv")
