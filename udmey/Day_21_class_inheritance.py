#Robot chef can bake,stir and measure
#A Pastry chef can do what Chef can do but do some extra things
#like knead(),whisk() etc.
#so we can inherit Chef class in Pastry Chef Class
#we can inherit attribute and behaviour

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale,exhale")

    def see(self):
        print("sea the see")

#Fish inherited Animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        #super().breath()
        # this replaces breathe function from Animal
        print("doing this under water")
    
    def swim(self):
        print("moving in water.")

    def see(self):
        # defining super above and using it here
        # will add the extra line in function see
        #from Animal class
        super().see()
        print("Sea the see again")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(f' number of eyes {nemo.num_eyes}')
nemo.see()


#class inheritance
#class Fish(Animal):
#    def __init__ (self):
#        super().__init__()
