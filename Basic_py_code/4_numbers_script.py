print(2)
print(3.14)
print(2+3.14)
print(3*4+5)  #17  BODMAS
print(3*(4+5)) #27
print(10%3)  #remainder 1

print("")
my_num = 5
print("printing number " + str(my_num)) # was gving error as my_num is number not like my_num="5" so made it str in print statement
print(abs(my_num))
print(pow(my_num,2)) # power function on variable my_num
print(max(my_num,6)) # maximium value is 6
print(min(my_num,6)) # minimum value is 5

print("")
print("if want to FROM MATCH IMPORT function like CEIL if not using this may get error")
print("name ceil is not defined")
from math import *
my_num = 4.5
print(ceil(3.7))
print(floor(my_num))
print(sqrt(36))
