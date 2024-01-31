enemies = 1  # this is global scope

def increase_enemies():
  enemies = 2                   # this is local scope
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#Dont modify the global scope varibale
# Global varibales as useful for constants like pi =3.14 (never gone change)


print(" ")
print ("Number guessing game")

print ("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
import random
In_computers_mind = random.randint(1,100)
#print(f' Computer choose {In_computers_mind}')
# global variables
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

difficult_type= input("Choose a difficulty Type 'easy' or 'hard' :")
if difficult_type == 'easy':
    attempt_count = EASY_LEVEL_TURNS
else:
    attempt_count = HARD_LEVEL_TURNS

while attempt_count >=1 :
    print(f'You have {attempt_count} attempts remaining to guess the number.')
    make_guess=int(input("Make a guess: "))
    if make_guess > In_computers_mind:
        print("Too High")
    elif make_guess < In_computers_mind:
        print("Too Low")
    elif make_guess == In_computers_mind:
        print (f'You got it the answer was {In_computers_mind}')
        attempt_count = 0

    attempt_count -= 1
    if attempt_count == 0:
        print(f' You have run out of guesses, you lose... number was {In_computers_mind}')
