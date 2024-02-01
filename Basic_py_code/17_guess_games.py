print("Guessing Game")
print("logic written by myself")
secret_word = "monkey"
guess=""    # initialize variable with null value
guess_limit = 3
guess_count = 0
while guess != "monkey" or guess_count <=3:
    if guess_count < guess_limit:
         guess = input("Enter the guess : ")
         guess_count += 1
         if guess == "monkey":
             print("you won")
             print("you won in " + str(guess_count) + " attempts")
             break  
    else:
        print("you have guessed 3 times wrong, you Loose")
        break
        
    
          
