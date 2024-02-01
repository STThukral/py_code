print("exponential function")
#simple exponential
print(2**3)
# exponential using function
def exp_func(base_num,power_num):
    return base_num**power_num


print(exp_func(3,3))


#creating exponential function
def expo_fn(base_num,power_num):
    result = 1
    for i in range(power_num):         #FOR loop example
        result = result * base_num
    return result


print(expo_fn(2,4))
