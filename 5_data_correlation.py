import pandas as pd
df=pd.read_csv("data_corr_5.csv")
print(df.to_string())

print(df.corr())


print("Result Explained")
print("The Result of the corr() method is a table with a lot of numbers")
print("that represents how well the relationship is between two columns")

print("The number varies from -1 to 1.")

print("1 means that there is a 1 to 1 relationship (a perfect correlation), and for")
print("this data set, each time a value went up in the first column, the other one went up as well.")

print("0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.")

print("-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.")

print("0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.")

print("What is a good correlation? It depends on the use, but I think it is safe to")
print("say you have to have at least 0.6 (or -0.6) to call it a good correlation.")

print("Perfect Correlation:")
print("We can see that Duration and Duration got the number 1.000000,")
print("which makes sense, each column always has a perfect relationship with itself.")

print("Good Correlation:")
print("Duration and Calories got a 0.922721 correlation, which is a very good correlation, and")
print("we can predict that the longer you work out, the more calories you burn, and the other way")
print("around: if you burned a lot of calories, you probably had a long work out.")

print("Bad Correlation:")
print("Duration and Maxpulse got a 0.009403 correlation, which is a very bad correlation, meaning")
print("that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.")



