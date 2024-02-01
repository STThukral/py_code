#using def means python knows we are going to use function
# : shows all the code will be inside function and it indents it by itself
#if indentation is done then it thinks function ends there
# function is good use when group of code performaing certain task and easly used many times
def say_hi():   
    print("Hello Dave")
def say_bye():   
    print("Bye Dave")

print("before function")
#using function
say_hi()
print("after function")
say_bye()


#parameterized function
def say_hello(name):
    print(" Hello " + name )
# more than one paramteres to function    
def say_hey(name,age):
    print(" Hey " + name + " you are " + str(age)) # str will be good for both age as string or integer

print("before function")
#using function
say_hello("Dave")
say_hello("sharad")
print("after function")
say_hey("Dave" ,"6")
say_hey("sharad","7")    

say_hey("Dave" ,8)
say_hey("sharad",45)    
