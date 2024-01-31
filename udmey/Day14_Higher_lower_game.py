import random
from hi_lo_gamedata import data

def fnc_compareA():
    compareA=[]
    retn_compareA=""
    var1=random.randint(0,len(data)-1)
    for key in data[var1]:
         compareA.append(data[var1].get(key))
    return compareA

def fnc_compareB():
    compareB=[]
    retn_compareB=""
    var1=random.randint(0,len(data)-1)
    for key in data[var1]:
         compareB.append(data[var1].get(key))
    return compareB

answer = True
score=0
count=1
swap_list=[]
while answer:
    if count ==1:
        compareA= fnc_compareA()
        print(f' CompareA: {compareA[0]}, {compareA[2]}, {compareA[3]}.')
        compareB= fnc_compareB()
        print(f' CompareB: {compareB[0]}, {compareB[2]}, {compareB[3]}.')
    else:         
         compareB= fnc_compareB()         
         while compareA==compareB:
            compareB= fnc_compareB()

         print(f' CompareB: {compareB[0]}, {compareB[2]}, {compareB[3]}.') 
 
    print(compareA[1])
    print(compareB[1])
    user_input= input("Who has more followers ? Type 'A' or 'B' :")
    print (user_input)
    
    if user_input =='A':
        if compareA[1] > compareB[1]:
           score +=1
           print(f'your score is {score}')
           swap_list = compareB
           print(f' CompareB: {swap_list[0]}, {swap_list[2]}, {swap_list[3]}.')
        else:
            print(f'Sorry, thats wrong.')
            answer = False
    elif  user_input =='B':
        if compareB[1] > compareA[1]:
           score +=1
           print(f'your score is {score}')
           swap_list = compareA
           print(f' CompareA: {swap_list[0]}, {swap_list[2]}, {swap_list[3]}.')
        else:
            print(f'Sorry, thats wrong.')
            answer = False
    count += 1       
print(f'Final Score :{score}')
