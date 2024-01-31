a=[1,2,3,4,5,6,7,8,9]
# -1 is start from back
# -4 is from back uptill 4 numbers
# -2 is skip 1 number and print 2nd number
p=a[-1:4:-2]
print (p)
p=a[-1:4:-1]
print (p)

print("########################")

# chracter to ASCII
# get the asci value
#var ='A'
#print (" ascii value of "+var+ " is :", ord(var));

var = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in var:
    print("Acsii value for " +str(i)+ " is : " ,ord(i))

# ASCII to charcter
# printing numeric to character value
for i in range(65,90):
    print ("Character value of " +str(i)+ " is : " , chr(i))


print("########################")

# shuffle function

# floor
print(5//2)
print(7.0//2)  #goes to lower value so 3
print(-7.0//2) #goes to lower value so -4


print("########################")

arr=[1,2,3]
print (arr) #call by value

print("########################")

#reverse the string
str="hello world"
str1= str[::-1]
print( str+" is now :")
print(str1)

def fnc_reverse(val):
    rev_val=val[::-1]
    print(" Reverse value of string : " +val+ " is : " +rev_val)

fnc_reverse('Dave Thukral')    


print(" Enter the string you want to reverse : ")
val=input()
rev_val=val[::-1]
print(" Reverse value of string : " +val+ " is : " +rev_val)

print("########################")

#find second largest number in list

my_list=[]
n=int(input("Enter your number : "))
for i in range (1,n+1):
    b=int(input(" Enter element :"))
    my_list.append(b)
    my_list.sort()
print ("Second largest number is : " , my_list[n-2])


      
print("########################")
#swappping list
#my_list=["Daddy","Mummy","Yashita","Dave"]
#size=len(my_list)
#print(size)
#print(my_list)
#temp=my_list[1]
#print(temp)
#my_list[1]=my_list[size-1]
#my_list[size-1] = temp

#print(my_list)


def replace_list_elements(num1,num2):
    my_list=["Daddy","Mummy","Yashita","Dave"]
    print(my_list)
    temp=my_list[num2]
    #print(temp)
    my_list[num2]=my_list[num1]
    my_list[num1] = temp
    #print(my_list[num1])
    #print(my_list[num2])
    return my_list


print(replace_list_elements(0,2))


print("########################")

# code to check vowels
# input string , check voewls from list
# find them and store them in list
# set final list, means make the list unique

def vowel_check(input_string,vowel_list):
    final_output=[]
    for i in input_string:
        if i in vowel_list:
            final_list.append(i)
            
    final_output = set(final_list)            # set removes duplicates from list
    print (" vowels in string : ", final_output)
            


vowel_list ="AEIOUaeiou"
final_list=[]
print (" enter the string to check vowels: ")
input_string = input()
vowel_check(input_string,vowel_list)
