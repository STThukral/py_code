
print("used return in function twice but one will executed")
print("user doesnt't enter first and last name it will give messeage at first retrun ")
def format(f_name,l_name):
    if f_name =="" and l_name=="":
        return "YOu should enter some value"
    full_name = f_name.title() +" "+ l_name.title()
    return full_name

format_name=format('sharad','thukral')
print(f'My full name is {format_name}')

#using foramt fucntion in print stement itself
print(format('shaRAd','tHUkral'))

#Asking for input in function parameter itself
print(format(input("What is your first name :"),input("What is your last name :")))


print("")
print("days in month, using year and month")
print("Also added Docstrings")
print("doumenation in code to tell what function does and will pop up message when using that function in code")

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
    
def days_in_month(year,month):
    #Docstring (write as many lines we wnat)
    """Take a first and last name and format it
        to return the title case version of the name"""
    if month > 12 or month <1:
        return "Please enter month between  1-12"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        return 29
    else:
        return month_days[month-1]

year= int(input("Enter the year : "))
month=int(input("Enter the month :"))
days=days_in_month(year, month)
print(days)



print("")
print(" calculator")
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    if n2 > n2:
        print ("result value will be negative (-)")
    return n1 - n2

def divide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2

def operation_type(operation,n1,n2):
    if operation == '+':
        return add(n1,n2)
    elif operation == '-':
        return subtract(n1,n2)
    elif operation == '/':
        return divide(n1,n2)
    elif operation == '*':
        return multiply(n1,n2)

answer = True
while answer:
    n1=int(input("Please enter first number : "))
    operation=input("Please enter the operation type +,-,/ or * :")
    n2=int(input("Please enter second number : "))
    result=operation_type(operation,n1,n2)
    print(f' Result value is : {result}')

    user_input = input(" Do you want to coninue y/n :")
    if user_input == 'n':
        answer = False
    
        
print(" ")
"""another way of making caluclator using dictonary is
   is really useful and with less line of code and dynamic using varaibles"""

print("")
print(" calculator")
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    if n2 > n2:
        print ("result value will be negative (-)")
    return n1 - n2

def divide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2

#dictonary used
operations= {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
    }

answer = True
while answer:
    n1=float(input("Please enter first number : "))
    for symbol in operations:
        print (symbol)
        #user will choose =,-,/ or *
    operation_symbol=input("Please pick the symbol from above :")
    n2=float(input("Please enter second number : "))
    # operation_symbol will be passed to dictionary as key to get resp. value
    operation_type=operations[operation_symbol]
    # use that value dynamically in to user add,subtract, multiply or divide only
    result=operation_type(n1,n2)
    print(f"{n1} {operation_symbol} {n2} is : {result}")

    user_input = input(" Do you want to coninue y/n :")
    if user_input == 'n':
        answer = False
