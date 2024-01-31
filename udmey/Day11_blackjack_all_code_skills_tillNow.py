import random
Keep_playing = True
user_card_list =[]
computer_card_list =[]
user_current_score=0
computer_current_score=0
"""used function to get randomn card , can call the fucntion when need new card
instead of calling random function again and again"""
def get_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
    
i=1
while Keep_playing:
    user_current_score =0
    computer_current_score=0
    if i == 1:
        # instead of i we cna use _ (underscore as we are not using i)
        for i in range(2):
            user_card_list.append(get_card())

    if i > 1:
        # Note fucntion is directly called in append instead of storing it into variable
        user_card_list.append(get_card())
                              
    computer_card_list.append(get_card())
    

    i +=1
    # instead of for loop we cna use SUM function as well (but this is just to see how it works in for
    # example SUM(user_card_list)
    for user_card_count in user_card_list:
         user_current_score += user_card_count
         
    for computer_card_count in computer_card_list:
         computer_current_score += computer_card_count     
    print(f'Your Cards: {user_card_list}, current score : {user_current_score}')
    print(f'Computer Cards: {computer_card_list}, current score : {computer_current_score}')

    user_input=input("Do you want to play a game of BalckJack ? Type 'y' or 'n' :")
    if user_input =='n':
        Keep_playing = False

    if  computer_current_score > user_current_score:
        print (" Computer won")
    elif user_current_score >  computer_current_score:
        print("User won")
    else:
        print("Draw")
