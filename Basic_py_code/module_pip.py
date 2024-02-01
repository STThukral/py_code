print("Module is where we create functions /procedure , varible declaration use in another py (python file")
print("MOdule with variable declaration, functions")
import random

feet_in_mile = 5280
meters_in_kilometers = 1000
beatles = ["john Lennon","Paul McCartney","George Harrison", "Ringo Star" ]


def get_file_txt(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1,num)
