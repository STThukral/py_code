# exercise 1 : when giving make_pie(4), as list is indexed utpo 2
# code will give error. execrcise is to handle this error

fruits = ["Apple","pear","Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]        
    except IndexError: # solution
        print("Fruit Pie")
    else:
        print(fruit + "pie")


print(fruits)
make_pie(4)
 


# exercise 2 : in this we are summing up Key Likes but at some places
# its comments and we will get error. as below
#Traceback (most recent call last):
#  File "C:/sharad/panda_scripts/udemy/30_error_exception_JSON_Data/30_exception_handling_exercise.py", line 35, in <module>
#    total_likes = total_likes + post['Likes']
#KeyError: 'Likes'
# we have to sort this error

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:  # solution
        #post['Commnets'] = 0 or another solution is
        #total_likes += 0     or another easy solution is use pass
        pass

print(f' Total likes are : {total_likes}')


# exercise 3: already created exercise and will make it effecient
#with try , except
# where user is trying to enter any values other than alphabets

import pandas as pd

#with open("nato_phonetic_alphabet.csv") as phoneic_file:
#    phoneic_words=phoneic_file.readlines()
#    print(phoneic_words)

data = pd.read_csv("nato_phonetic_alphabet.csv")
print(data)

phoneic_dict ={row.letter:row.code for(index,row) in data.iterrows()}
print(phoneic_dict)

# adding code in function so that we can call it again
# in case of user entered values other than alphabets
# and in except displaying message and running function again
# and else printing it if all is correct
def generate_phonetic():
    user_word = input("please enter the word : ").upper()
    #print(user_word)

    try:
        user_list = [phoneic_dict[letter] for letter in user_word]
    except:
        print("Sorry only letters in alphabets please")
        generate_phonetic()
    else:
        print(user_list)


generate_phonetic()
