print(" ")
print("str")   #"123","string"
print("int")   # 123
print("float") #3.1234
print("boolean") # True/False (initial capital)

print(" ")
print("Good example for float and int DATA TYPES")

print("Welcome to the tip Calculator.")
cust_bill_amt=input(" what was the total bill ? £")
cust_count=input("How many people to split the bill ? ")
discount_perc=input("What percentage tip would you like to give ? 10, 12, or 15 ?")
percentage_amt =(float(cust_bill_amt) * int(discount_perc)) /100
bill_to_pay=float(cust_bill_amt)+ float(percentage_amt)
invidual_bill_amt=int(bill_to_pay)/int(cust_count)
print("Each person should pay : £" , round(invidual_bill_amt,2))
print("Each person should pay : £{:.2f}".format(invidual_bill_amt)) #force to give 2 decimals 

print(" ")
print ("123" + "456")  #123456
print (int(123) + int(456)) #579

mystery =734_529.678
print(mystery)  # even though underscore will not effect it

print(type(mystery)) # to invetigate the datatype


print(" ")
print(" enter 2 digit number and sum 2 digts to get result")
two_digit_num = input("Enter 2 digit number : ")
sum_of_two_digit = int(two_digit_num[0]) + int(two_digit_num[1])
print (" Sum of entered 2 digit number " + two_digit_num + " is " , sum_of_two_digit)

#BODMAS
# 3 + 5 addition
#7-2 subtraction
print (3*2) #multiply
print (6/2) # divide and answer will be float
print(2**3) # 2 to the power of 3

print( 3 * 3 + 3 / 3 - 3)  #7.0
print (3 * (3+3)/3 -3) #3.0

print(round(8/3,2))
print(8//3) # floor



print("Body Mass index calculation")
height=input("Enter your height in m :")
weight=input("Enter your weight in kg : ")
BMI= float(weight) / (float(height)**2)
print(" your BMI is : ", int(BMI))


print(" f-string ")
score=0
score += 1
print(score)
print(f' your score is {score}') #OR below one both works
print(f"your score is {score}")


age=int(input("What is your current age :"))
age_limit=int(90)
age_left= age_limit -age
days_remaining = age_left *365
week_remaining= age_left *52
months_remaining =age_left *12
message=f' you have {days_remaining} days, {week_remaining} weeks, {months_remaining} months'
print(message)
