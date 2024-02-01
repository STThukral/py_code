print("Inheritance is where we define a buch of arritbute and function")
print("inside a class and create another class which will inhert all the attribute")
from chef_30 import chef
from chineseChef_30 import ChineseChef

mychef = chef()
mychef.make_chicken()  #calling make_chicken function from class_30
mychef.make_special_dish()  #calling make_special_dish function from class_30

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()  #calling make_special_dish function from chineseChef_30
myChineseChef.make_chicken()  #now calling make_chicken function in Chef_30 inherited by chineseChef_30 script
myChineseChef.make_special_dish()  #inherited from chef_30 and overwritten in ChineseChef_30
