import pandas as pd
import random
from wordlist import word_list
from hangman_pic import hangman
from IPython.display import clear_output
import os
from time import sleep
#print(word_list)
target_word = random.choice(word_list).lower()
#print (target_word)

display_word= []
for letters in target_word:
    display_word += '_'

print(display_word)
character_already_guessed = [ ]

game_over = False
lives = 7
count = 0
while game_over == False:
    user_guess = input("Please Guess the letter : ")
    print(user_guess)
    character_already_guessed.append(user_guess)
    char_already_gussed_unique_val = set(character_already_guessed)
    
    #if user_guess in char_already_gussed_unique_val:
    print(f'character already entered : {char_already_gussed_unique_val}')
    
    #clear_output(True)
    #clear_output(wait=True)
    #count +=1
    if user_guess in display_word:
        print ('This letter already guessed, please try again')
        print ('!! NO LIVES LOST !!')

    if user_guess in target_word:
        for position in range(len(target_word)):
           if user_guess == target_word[position]:
              display_word[position] = user_guess
              print(display_word)
    else:
        if character_already_guessed.count(user_guess) > 1:
                print ('Character already entered.. NO lives lost !!')
        else:                
               lives -= 1        
               print (hangman [lives])        
               print('lives remaining :' , lives)
               print(display_word)
               if lives == 0:
                  game_over = True
                  print('---------------')
                  print('---------------')
                  print(' !! GAME OVER, you lost the Game !!')
                  print(' Correct answer is : ' ,target_word)
                  print('---------------')
                  print('---------------')

    if '_' not in display_word:         
         print(' HURRAY .. YOU WON !! ')
         game_over = True

