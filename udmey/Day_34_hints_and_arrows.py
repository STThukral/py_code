# beow code is to show how we use Type HINT and arrwos
#to define the variable type and reurn value type
# we can define datatype of age as below
age: int
age=12
print(age)

print(type(age))
# above will print it as int

name: str
height: float
is_human: bool


def police_check(age):
    if age > 18:
        can_drive = True
    else:
        can_drive =False
    return can_drive

if police_check(19):
    print("you can drive")
else:
    print("Pay a fine")
    

#we can use arrw as well as datatype declaration
# Also we can declare datatype of retrun value as well like bool
def police_check_1(age: int) -> bool:
    
    if age > 18:
        can_drive = True
    else:
        can_drive =False
    return can_drive

if police_check_1(18):
    print("you can drive")
else:
    print("Pay a fine")





def greetings(name: str) -> str:
    return 'Hello ' + name

print(greetings('sharad'))
print(greetings(1234))
#TypeError: can only concatenate str (not "int") to str
#for above 1234 as its number expecting string
