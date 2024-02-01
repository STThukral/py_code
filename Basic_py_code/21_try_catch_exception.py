print("Try Catch exception using Try except clause")
#incase user enters character instead of number in input

try:
   num = int(input("Enter the number : "))
   print (num)
except:
    print("please enter valid value i.e. number as value")


print("")
print("More than one except for different line of code,with specific error")

try:
   v = 10/1 # seperate excpetion for this as 10/0
   num = int(input("Enter the number : ")) # seperate exception this
   print (num)
except ZeroDivisionError:         #ZeroDivisionError copied from error itself
    print("Divided by zero") 
except ValueError:                #ValueError copied from error itself  
    print("please enter valid value i.e. number as value")
