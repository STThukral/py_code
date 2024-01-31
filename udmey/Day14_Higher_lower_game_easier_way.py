import random
from hi_lo_gamedata import data


score =0

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    #print(account_a)
    #print(account_b)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"CompareA :{format_data(account_a)}.")
    print("vs")
    print(f"AgainstB :{format_data(account_b)}.")

    guess=input("Who has more followers? Type 'A' or 'B' :").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct =check_answer(guess,a_follower_count,b_follower_count)

    if is_correct:
        score +=1
        print(f"you're right! current score: {score}")
    else:
        print("Sorry,that's wrong.")
        game_should_continue=False
print(f'your score is {score}')
