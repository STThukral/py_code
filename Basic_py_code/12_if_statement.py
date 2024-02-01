#IF statements

#IF
#ELIF
#ELSE   (will be default statement)
# notice there is no end of IF like in unix FI or oracle END IF

is_male = True
is_tall = True

if is_male or is_tall:
    print("you are a Male or Tall")
else:
    print("you are not Male nor Tall")

is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a Tall Male")
elif is_tall:
    print("you are tall but not Male")
elif not(is_tall):                          # if is_tall = False
    print("you are not tall")
else:
    print("you are not Tall Male")


i=6
if i > 1 and i <= 5:
    print ( " i is greater than 1 but less than equal to 5")
else:
    print(" i is more than 5")



            
    
