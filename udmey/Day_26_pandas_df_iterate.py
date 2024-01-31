student_dict = {
    "student":["Angela","james","Lilly"],
    "score": [56,76,98]
    }

# for loop iteration for dictionary
for (key,value) in student_dict.items():
    print(key)
    print(value)


# gettign dictionary in dataframe
import pandas as pd
df = pd.DataFrame(student_dict)
print (df)

# we can iterate it as well
for(key,value) in df.items():
    print(key)
    print(value)

# But there isanother way to iterate using inbuild loop ITERROWS loop
for (index,row) in df.iterrows():
    #print(index)
    #print(row)
    # Also we can use if condirion
    if row.student == "james":
        print(f' Student {row.student} score is {row.score}')
