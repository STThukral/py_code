import time
#print(time.time())
current_time=time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f" {function.__name__} run_speed: {end_time - start_time}s ")
    return wrapper_function    

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i +=i


@speed_calc_decorator
def slow_function():
    for i in range(5000000):
        i +=i
    

fast_function()
slow_function()


# first define fast and slow functions and then create decorator function
# which basically adding extra fucntionality in slow and fast function processing
#i.e. calculating start and end time for each function

#Defination
#Python Decorators
#In Python, a decorator is a design pattern that allows you to modify the
#functionality of a function by wrapping it in another function.

#The outer function is called the decorator, which takes the original
#function as an argument and returns a modified version of it.


#They are an excellent way to apply reusable functionality across
#multiple functions, such as timing, caching, logging, or authentication.
#logging, debugging, authentication, measuring execution time
