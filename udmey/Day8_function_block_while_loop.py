def greet():
    print("Hello")
    print("welcome")

greet()


def greet_with_name(name,loc):
    print(f'Hello {name}')
    print(f'welcome {name}, how is weather in {loc}')

greet_with_name("Dave","bracknell")            #argument with position
greet_with_name(loc="bracknell",name="sharad") #arguments with keyword


for i in range(1,101):
    if  i==2 or i==3:
        print(f'Number {i} IS PRIME')
    elif  i==1 or i%2 == 0 or i%3 ==0:
         print(f'Number {i} is not prime')
    else:
         print(f'Number {i} IS PRIME')


# enter the alphabests twice becuase if we enter encrypt_fn('xmfwfi',5)
# i.e. encrypt x there is no rnage after x+5 i.e 22 + 5 is 27 letter are upto 25
alphabets = ['a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
             'a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
             ]

user_input=input("Please enter the alphabet : ")
pos_of_input= alphabets.index(user_input)

print (pos_of_input)
new_pos=int(pos_of_input)+5
print(new_pos)
new_alphabet= alphabets[new_pos]
print(new_alphabet)

print("")
print(" encrypt a character to next 5th and decrypt it back")
def encrypt_fn(user_input,shift_amount):
    final_encryption=""
    shift_amount=5
    #user_input=input("Please enter the string : ")
    for letter in user_input:
        pos_of_input= alphabets.index(letter)
        #print (pos_of_input)
        new_pos=int(pos_of_input)+shift_amount
        #print(new_pos)
        new_alphabet= alphabets[new_pos]
        final_encryption += new_alphabet
    print (f' String was entered as  : {user_input}')
    print(f' Encrypted output string : {final_encryption}')


def decrypt_fn(user_input,shift_amount):
    final_decryption=""
    shift_amount=5
    for letter in user_input:
        pos_of_input= alphabets.index(letter)
        #print (pos_of_input)
        new_pos=int(pos_of_input) -shift_amount
        #print(new_pos)
        new_alphabet= alphabets[new_pos]
        final_decryption += new_alphabet
    print(f' Encrypted output string : {final_decryption}')

encrypt_fn('sharad',5)
decrypt_fn('xmfwfi',5)
encrypt_fn('xmfwfi',5)
