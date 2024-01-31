print("find even or odd")
print(" ")

user_number=float(input("please enter the number, will check its even or odd :"))
even_odd = user_number%2
if even_odd == 0:
    print(f' {user_number} is even')
else:
    print(f'{user_number} is odd')

                  
print(" ")
print("BMI index with message ")
weight=int(input("Please enter your weight : "))
height=float(input("Please enter your height :"))
BMI_cal=weight/(float(height)**2)
print(f'Your BMI is {BMI_cal}')
if BMI_cal <= 18.5:
    print("Under 18.5 they are underweight")
elif BMI_cal > 18.5 and BMI_cal < 25 :
    print("Over 18.5 but below 25 they are normal weight")
elif BMI_cal > 25 and BMI_cal < 30 :
    print("Over 25 but below 30 they are overweight")
elif BMI_cal > 30 and BMI_cal < 35 :
    print("Over 30 but below 35 they are obese")
elif BMI_cal > 35:
    print("Above 35 they are clinically obese")


print(" ")
print("Welcome to the python Pizza Delivery!")
size=input("What size pizza do you want ? S,M or L :")
add_pepperoni=input("Do you want pepperoni ? Y or N :")
extra_cheese=input("Do you want extra cheese ? Y or N :")


    
if size == 'S':
    amount =15
elif size == 'M':
    amount =20
elif size == 'L':
    amount =25

if add_pepperoni == "Y":
    if size =="S":
        amount += 2
    else:
        amount += 3

if extra_cheese =="Y":
    amount += 1
           
print(f'Your final bill is: ${amount}')

print("                   ")

print("")
print("Love calculator")
name1=input("What is your name : ")
name2=input("What is their name :")

combined_string = name1 + name2
lower_case_string= combined_string.lower()
    
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

first_perc = t+r+u+e
second_perc =l+o+v+e

final_perc= str(first_perc)+ str(second_perc)

             
if int(final_perc) < 10 or int(final_perc) > 90:
    print(f' Your score is {final_score}, you got togrther like coke and mint')
elif int(final_perc) >=40 and int(final_perc) <=50:
    print(f'Your score is {final_perc}, you are alright together')
else:
    print(f' Total percentage is {final_perc}')
