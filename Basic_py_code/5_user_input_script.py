print("user input script")
#input("Enter your Name : ")
name = input("Enter your name :")
print("Hello " +name)
age = input("Enter your age : ")
print("Hello " +name +" you are " +age)

print("")
print("basic calculator")
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

# specify num1 and num2 specifically int
#result = int(num1) + int(num2)
#make it float so that can enter num1 and num2 in decimals this will not
#give error when trying to enter decimal value in INT
result = float(num1) + float(num2)
# as result is INT now but will not got with string then make STR below
print(" sum of num1 and num2 is " +str(result))


