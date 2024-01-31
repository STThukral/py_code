import pandas as pd


print("Big data sets are often stored, or extracted as JSON.")

print("JSON is plain text, but has the format of an object, and is ")
print("well known in the world of programming, including Pandas.")
print("JSON objects have the same format as Python dictionaries.")
df=pd.read_json('data3.json')
print(df.to_string())

print("Analyze data")

print(" print first 10 rows with Header, like unix head -10")
print(" if we use just df.head or df.tail it will retrun frist 5 or last 5 resp.")
df = pd.read_csv('data_file1.csv')
print (df.head(10))

print(" print last 10 rows, like unix tail -10")
df = pd.read_csv('data_file1.csv')
print (df.tail(10))


print (" get info about Data")
print(df.info())

#IMP
#The info() method also tells us how many Non-Null values there are present in each
#column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
#Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

#Empty values, or Null values, can be bad when analyzing data, and you should consider
#removing rows with empty values. This is a step towards what is called cleaning data,
#and you will learn more about that in the next chapters.

# NOTE :- look in output of print(df.to_string()) , will see NaN agaisnt null value
