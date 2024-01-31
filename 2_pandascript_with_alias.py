import pandas as pd
print("panda script with alias pd")

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)    # pd alias 

print(myvar)


# check pandas version
#import pandas as pd        # not needed as already declared up


print(" ")

print("pandas version ")
print(pd.__version__)


print("A Pandas Series is like a column in a table.")

print("It is a one-dimensional array holding data of any type.")

print("---Series---------")
a = [2, 7, 5]

myvar=pd.Series(a)  # remember function are case senstive e.g Series
print(myvar)
print(myvar[0])   # print first value i.e 2
print("--------")


print("---we can give our own indexes like above indexes are 0,1,2 and so on whne we run Series-----")

myvar=pd.Series(a,index = ["a","b","c"])
print(myvar)
print(myvar["a"])


print("")
print("--------")
print("")
print("keys and values same as dictionary but printed in Series jan is key and January is Value and so on")
print("another example, datatype will be OBJECT as values are characters")
monthconversion = {
    "Jan" : "january",
    "Feb" : "February",
    "Mar" : "March"}
                
myvar=pd.Series(monthconversion)
print(myvar)

print("")
print("another example, datatype will be int64 as values are integer")
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

print("")
print(" --index argument and specify only the items you want to include in the Series--")
print("day3 excluded from Series")
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


print("")
print("")
print("--DataFrame")
print("Data sets in Pandas are usually multi-dimensional tables, called DataFrames.")

print("Series is like a column, a DataFrame is the whole table.")


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

print("")
print("Pandas use the loc attribute to return one or more specified row(s)")
print("refer to the row index by Named index:")
print(myvar_df.loc["a"])  # NOTE : as we have manually indexed it a,b,c thus used "a" otherwise would have 0


print("")
print("another example")
#use a list of indexes:
print(myvar_df.loc[["a", "b"]])


print("")
print("Load a comma separated file (CSV file) into a DataFrame:")
df = pd.read_csv('data_file.csv')

print(df) 



print("")
print("Load a comma separated file (CSV file) into a DataFrame big file:")
print("As its big file print(df) will return first 5 and last 5 records:")
df = pd.read_csv('data_file1.csv')
print(df) 



print("")
print("Load a comma separated file (CSV file) into a DataFrame big file:")
print("As its big file to return all records (i.e. entire data frame in file do below:")
df = pd.read_csv('data_file1.csv')
print(df.to_string())

print (" this will give 60 and we can increase it as well and then use print(df)")
print ("data_file1.csv")
print(pd.options.display.max_rows) 

pd.options.display.max_rows = 999
print(df)

print("")
print(" Reading csv file with header =0 and column seperator")
print("header=0 means that the headers for the variable names are to")
print("be found in the first row (note that 0 means the first row in Python")
print(" comma Seperator is used as the separator between the values")
print("This is because we are using the file type .csv  i.e. comma separated values")

df=pd.read_csv("data_file1.csv",header=0 , sep=",")
print(df.to_string)

