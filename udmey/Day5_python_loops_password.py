import math
fruits ={"banana","apple","orange"}
for fruit in fruits:
    print(fruit)


print(" ")
print("Find Avg student height")
student_sum=0
student_count=0
students_heights= [180,124,165,173,189,169,146]
for students in students_heights:
    student_sum = student_sum + int(students)
    student_count += 1

#no_of_students=len(students_heights)
#student_sum=sum(students_heights)
# can use len but as per
#exercise requirement count students in loop
#print(f' No. of student are : {no_of_students}')
#Avg_student_height= math.ceil(student_sum / no_of_students)
Avg_student_height= math.ceil(student_sum / student_count)
print(f' Total of student Heights is : {student_sum}')
print(f' Total of student Heights is : {student_count}')
print(f' Average student Heights is : {Avg_student_height}')



print(" ")
print(" Heighest value in class ")

student_scores=[78,65,89,86,55,91,64,89]
#print(max(student_scores))
#print(min(student_scores))
max_num=0

for scores in student_scores:
    if int(scores) > max_num:
        max_num = scores
print(f' Max value is : {max_num}')


print(" ")
num=0
print(" For loop range operator")
# 1, 101 means 1 till 100 becuase last digit is not included
for i in range(1,101):
    num += i
print(num)



print(" ")
num=0
print(" For loop range operator to sum even numbers")
# 1, 101 means 1 till 100 becuase last digit is not included
for i in range(1,101):
    if i%2 == 0:
        num += i
print(num)


print(" ")
num=0
print(" Another way of sum even numbers is")
# 1, 101 means 1 till 100 becuase last digit is not included
#range(2,101,2) menas sum value 2 i.e starat from even to 100
#and skip 1 number and move to second i.e. even
for i in range(2,101,2):
        num += i
print(num)

print(" ")
print(" FizzBuzz Game")
# id number divisible by 3 then Fizz
# if number divisible by 5 then Buzz
# if number divisible by 3 and 5 both then FizzBuzz
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print (f' number is {i} :FizzBuzz')
    elif i%3 == 0:
        print (f' number is {i} :Fizz')
    elif i%5 == 0:
        print (f' number is {i} :Buzz')
    else:
        print (f' number is {i} : {i}')
    
 
print (" ")
print("Random password generation ")
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
           ,'n','o','p','q','r','s','t','u','v','w','x','y','z'
           ,'A','B','C','D','E','F','G','H','I','J','K','L','M'
           ,'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols= ['!','£','$','%','^','&','*','(',')','_','+']

print("Welcome to the password generator!")
nr_letters=int(input("How many letter would you like in your password ?\n"))
nr_numbers=int(input("How many numbers would you like in your password ?\n"))
nr_symbols=int(input("How many symbols would you like in your password ?\n"))

random_passwd_list= []
for char in range(1,nr_letters+1):
    random_passwd_list.append( random.choice(letters))

for num in range(1,nr_numbers+1):
    random_passwd_list.append(random.choice(numbers))

for symb in range(1,nr_symbols+1):
    random_passwd_list.append(random.choice(symbols))
print(random_passwd_list)
random.shuffle(random_passwd_list)

passwd=""
for i in random_passwd_list:
    passwd += i
print(f' Your new password is : {passwd}')
