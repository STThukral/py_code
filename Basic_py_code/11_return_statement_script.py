print("RETURN STATEMENT")
# like function return some value

def cube_num(num):
    return num*num*num   # once return used no code will work after it
    print(" cube of num done") # will not be printed

print(cube_num(3))
print(cube_num(4))

result = cube_num(5) # use the return value in variable
print("result is  :" + str(result))


def cube_num1(num):
    print("cube of num is under function cube_num1 : " +str(num*num*num))
    # Below print statement will be printed
    print("cube of num done using function cube_num1")


    
cube_num1(3)
cube_num1(9)
