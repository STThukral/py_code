print("Make advance calculator")
num1 = float(input("enter first number : "))
op = input("Enter the operator : ")
num2 = float(input("enter first number : "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
