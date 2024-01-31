number = [1,2,3]
new_list = []
for num in number:
    add_1 = num +1
    new_list.append(add_1)

print(new_list)

# List comprehension by getting similar result as above in 1 line
number = [5,6,7]
#new_list = [new_item for item in list]
#new_list is output result in list
#new_item what we want to do with "list"
#for item in list is a loop
new_list_1 = [num+ 2 for num in number]
print(new_list_1)


name ="sharad"
new_letters_list = [letter for letter in name]
print(new_letters_list)


double_num = [n*2 for n in range(1,5)]
print(double_num)


#conditional list comprehension
#new_list = [new_item for item in list if Test]

names=["Alex","Beth","Carolina","Dave","Freddie","Jack","jane"]
print(names)
# check the list loop through it and if name is of length =4 then add in
# in list four_letter_word_list 
four_letter_word_list = [name for name in names if len(name) == 4]
print(four_letter_word_list)

#get the name from list length greater than 4 and make it in capital letters
gt_4_list_in_caps = [name.upper() for name in names if len(name) > 4]
print(gt_4_list_in_caps)

# PRACTICE List comprehension

numbers = [1,1,2,3,5,8,13,21,34,55]
squared_list = [n*n for n in numbers]
#squared_list = [n**2 for n in numbers] or we can use this n**2
print(squared_list)

#only even numbers from above list
even_list = [n for n in numbers if n%2 == 0]
#squared_list = [n**2 for n in numbers] or we can use this n**2
print(even_list)

file1_list=[]
with open("Day26_file1.txt") as file1:
    file1_nums = file1.readlines()
    for rows in file1_nums:
        file1_list.append(int(rows))
        
file2_list=[]
with open("Day26_file2.txt") as file2:
    file2_nums = file2.readlines()
    for rows in file2_nums:
        file2_list.append(int(rows))

print(file1_list)
print(file2_list)

common_list = [n for n in file1_list if n in file2_list]
print(common_list)
        
    
