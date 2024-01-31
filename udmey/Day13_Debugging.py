def my_function():
    for i in range(1,20):
        #print(i)
        # this will never print becuase it runs range(1,20) run from 1..19
        # and dosent include 20,make range (1,21)
        if i == 20: 
            print("you got it")

my_function()


import random
dice_imgs = ["0","1","3","4","5","6"]
#dice_num=random.randint(0,5) #if you give (1,6) it will give 6 at somepoint
#randint include starts and end number not like range
#and there is no index value for 6 as list starts form 0 so make (0,5)
dice_num=random.randint(0,5)
print(dice_imgs[dice_num])


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # if you not append it you will get on 26 i.e. last value
    print(b_list)

mutate([1,2,3,5,8,13])
            
