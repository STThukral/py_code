print("compare numbers and string")
def max_num(param1,param2,param3):
    if param1 >= param2 and param1 >= param3:
        print(str(param1) + " is the biggest number")
        return param1
    elif param2 >= param1 and param2 >= param3:
        print(str(param2) + " is the biggest number")
        return param2
    else:
        print(str(param3) + " is the biggest number")
        return param3

print(max_num(80,10,60))
print(max_num(100,110,120))
print(max_num(90,10,60))


print("compare string") # use double equal sign ==
