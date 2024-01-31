#comprehension dictionary
#new_dict={new_key:new_value for item in list}

# new dictionary using existing dictionary
#new_dict={new_key:new_value for(key,value) in dict.items()}


# new dictionary using existing dictionary with if condition
#new_dict={new_key:new_value for(key,value) in dict.items() if test}


import random

names=["Alex","Beth","Carolina","Dave","Freddie","Jack","jane"]
print(names)

# in below getting names from "names" list and creating
# names as key and value as random number between 1, 100
# as there marks
student_score ={student:random.randint(1,100) for student in names}
print(f'student_score => {student_score}')


# from above created dictionary we will decide who passsed
# and didn't

passed_students = {student_name:student_score for(student_name,student_score) in student_score.items() if student_score >= 50}

print (f' passwd_students => {passed_students}')


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Step 1 :- spliting above sentence and making a list
# Step 2 :- making dictionary by using new_list
#           each word as key and length of word as value
print(sentence)
new_list =[]
new_list = list(sentence.split(" "))
print(new_list)                
# Write your code below:
result= {word:len(word)  for word in new_list}
print(result)


# Another way to write above with less lines is
# Use SPLIT in comprehension dictionary line itself , this will save
# some line and there is  no need to create new_list as well
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Step 1 :- making dictionary by using by spliting sentence into words
#           each word as key and length of word as value
print(sentence)
# Write your code below:
result= {word:len(word)  for word in sentence.split()}
print(f' new result is => {result}')


print(" ")

print("Weather in Celsisus")
# Dictionary of Degree of Celsius to Degree of Faherenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
print(weather_c)
# Write your code 👇 below:
weather_F ={weather_day:(weather_temp_c *9/5) +32   for (weather_day,weather_temp_c) in weather_c.items()}

print(f'weather in Faherenheit => {weather_F}')

