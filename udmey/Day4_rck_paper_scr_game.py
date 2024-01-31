from rock_paper_scissor_choice import choices
import random

#Player2=random.randint(0,2) # here Player 2 is kind of computer now
Player1=int(input("Player1 Please enter your choice 0 to 2:"))
Player2=int(input("Player2 Please enter your choice 0 to 2:"))


print(f'Player 1 entered : {Player1} that is {choices[Player1]}')
print(f'Player 2 entered : {Player2} that is {choices[Player2]}')

if Player1 == 0 and Player2 ==1:
    print(f'Player2 won')
elif Player1 == 0 and Player2 ==0:
    print(f' NO ONE won')
elif Player1 == 0 and Player2 ==2:
    print(f' Player1 won')
elif Player1 == 1 and Player2 ==0:
    print(f' Player1 won')
elif Player1 == 1 and Player2 ==1:
    print(f' NO ONE won')
elif Player1 == 1 and Player2 ==2:
    print(f' Player 2 won')
elif Player1 == 2 and Player2 ==1:
    print(f' Player1 won')
elif Player1 == 2 and Player2 ==2:
    print(f' NO ONE won')
elif Player1 == 2 and Player2 ==0:
    print(f' Player 2 won')

