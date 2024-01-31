#default arguments

def foo(a,b=4,c=6):
    print(a,b,c)

foo(1)


def foo(a,b=4,c=6):
    print(a,b,c)

foo(4,9)

def foo(a,b=4,c=6):
    print(a,b,c)

foo(4,9)


def foo(a,b=4,c=6):
    print(a,b,c)

foo(20,c=6)

#unlimited arguments using * insetead of args we can give any name
#unlimited position arguments
def add(*args):
    total_sum=0
    for n in args:
        total_sum =  total_sum + n
    return(total_sum)


print(f' Total sum of numbers are {add(3,5,6,7,1)}')


print("")
#kwargs is "key word arguments"
# names the values passed to the function **kwargs
# all named paramters comes under **kwargs like add=3,multiply=5

def calculate(**kwargs):
    print(kwargs) # this gives dictionary
    #{'add': 3, 'multiply': 5}

calculate(add=3,multiply=5)

print("")
def calculate(n,**kwargs):
    n += kwargs["add"]        # 2+3 =5
    n *= kwargs["multiply"]   # 5*5 =25
    print(f' Final result is : {n}')
    
calculate(2,add=3,multiply=5)


class Car:
    
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model= kw["model"]

my_car =Car(make ="Nissan",model="GTX")
print(f' car model : {my_car.model}')
print(f' car make : {my_car.make}')

print("")
print("")

# if we miss the model in parameter but in self
# it will  give error
# avoid that error use get function in this for model it will give None
class Car:
    
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model= kw.get("model")

my_car =Car(make ="Nissan")
print(f' car model : {my_car.model}')
print(f' car make : {my_car.make}')


        
